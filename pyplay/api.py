# SPDX-FileCopyrightText: 2020-2026 Aurora OSS
# SPDX-FileCopyrightText: 2023-2025 The Calyx Institute
# SPDX-FileCopyrightText: 2021-2026 David Weinstein, Electronic Frontier Foundation
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import base64
import json
import logging
import secrets
from dataclasses import dataclass, fields
from io import BytesIO
from itertools import count
from time import perf_counter
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar
from zipfile import ZipFile

import httpx
from babel import Locale, default_locale
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import DecodeError, Message

from pyplay.constants import (
    DEFAULT_ANDROID_VENDING_APP,
    DEFAULT_ANDROID_VENDING_PACKAGE,
    DEFAULT_CALLER_SIG,
    DEFAULT_CLIENT_SIG,
    DEFAULT_DFE_PHENOTYPE,
    DEFAULT_DFE_TARGETS,
    LEGACY_USER_AGENT,
    URL_ACQUIRE,
    URL_AUTH,
    URL_BULK_DETAILS,
    URL_CATEGORIES,
    URL_CHECK_IN,
    URL_DELIVERY,
    URL_DETAILS,
    URL_FDFE,
    URL_LIBRARY,
    URL_MODIFY_LIBRARY,
    URL_PURCHASE,
    URL_PURCHASE_HISTORY,
    URL_REVIEW_ADD_EDIT,
    URL_REVIEW_DELETE,
    URL_REVIEW_USER,
    URL_REVIEWS,
    URL_SEARCH,
    URL_SEARCH_SUGGEST,
    URL_TESTING_PROGRAM,
    URL_TOC,
    URL_TOP_CHART,
    URL_TOS_ACCEPT,
    URL_UPLOAD_DEVICE_CONFIG,
    URL_USER_PROFILE,
    DeliveryResponseStatus,
    PatchFormat,
    PlayFileType,
    ReviewFilter,
    StreamCategory,
    StreamType,
    TokenService,
)
from pyplay.device import Device
from pyplay.exceptions import AuthExceptionError, EmptyDownloadsError, ProtobufResponseError, PurchaseError
from pyplay.playprotos.acquire_app import AcquireRequest, AcquireResponseWrapper
from pyplay.playprotos.google_play import (
    AndroidCheckinResponse,
    BulkDetailsRequest,
    ModifyLibraryRequest,
    ResponseWrapper,
    ResponseWrapperApi,
    TestingProgramRequest,
    UploadDeviceConfigRequest,
)
from pyplay.playprotos.stream import StreamResponse

T = TypeVar("T", bound=Message)


if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path
    from types import TracebackType

    from pyplay.constants import CategoryType, MyAppsClusterType
    from pyplay.playprotos.google_play import (
        AcceptTosResponse,
        BrowseResponse,
        BulkDetailsEntry,
        DeliveryResponse,
        DetailsResponse,
        Item,
        ListResponse,
        Review,
        ReviewResponse,
        SearchSuggestResponse,
        TestingProgramResponse,
        TocResponse,
        UploadDeviceConfigResponse,
        UserProfile,
    )


logger = logging.getLogger(__name__)
_REQUEST_IDS = count(1)
_TOKEN_PREVIEW_MIN_CHARS = 12
_TOKEN_PREVIEW_EDGE_CHARS = 3


def _token_preview(value: str) -> str:
    if len(value) < _TOKEN_PREVIEW_MIN_CHARS or not all("!" <= char <= "~" for char in value):
        return "<redacted>"
    return f"{value[:_TOKEN_PREVIEW_EDGE_CHARS]}…{value[-_TOKEN_PREVIEW_EDGE_CHARS:]}"


def _safe_route(url: str) -> str:
    try:
        route = httpx.URL(url).path
    except (httpx.InvalidURL, ValueError):
        return "<invalid>"
    return route.encode("unicode_escape").decode("ascii") or "/"


def _fdfe_url(path: str) -> str:
    base = httpx.URL(f"{URL_FDFE}/")
    url = base.join(path)
    if (url.scheme, url.host, url.port) != (base.scheme, base.host, base.port):
        msg = "Stream URLs must use the Google Play API origin"
        raise ValueError(msg)
    return str(url)


def _elapsed_ms(started: float) -> int:
    return int((perf_counter() - started) * 1000)


def _raise_for_status(response: httpx.Response, method: str, route: str) -> None:
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError:
        msg = f"{method} {route} returned HTTP {response.status_code}"
        raise httpx.HTTPStatusError(msg, request=response.request, response=response) from None


def _decode_response(message_type: type[T], response: httpx.Response, method: str, route: str) -> T:
    try:
        return message_type.FromString(response.content)
    except DecodeError:
        raise ProtobufResponseError(method, route) from None


def _stream_list_response(response: ResponseWrapper) -> ListResponse:
    if (
        response.HasField("pre_fetch")
        and response.pre_fetch.HasField("response")
        and response.pre_fetch.response.HasField("payload")
        and response.pre_fetch.response.payload.HasField("list_response")
    ):
        return response.pre_fetch.response.payload.list_response
    return response.payload.list_response


@dataclass(repr=False)
class AuthData:
    email: str = ""
    aas_token: str = ""
    gsf_id: str = ""
    auth_token: str = ""
    oauth_login_token: str = ""
    ac2dm_token: str = ""
    android_check_in_token: str = ""
    device_check_in_consistency_token: str = ""
    device_config_token: str = ""
    experiments_config_token: str = ""
    gcm_token: str = ""
    dfe_cookie: str = ""

    def __repr__(self) -> str:
        hidden_fields = {"email", "gsf_id", "dfe_cookie"}
        values = []
        for field in fields(self):
            value = getattr(self, field.name)
            preview = "<redacted>" if field.name in hidden_fields else _token_preview(value)
            values.append(f"{field.name}={preview!r}")
        return f"AuthData({', '.join(values)})"


@dataclass(repr=False)
class PlayFile:
    name: str
    url: str
    size: int
    type: PlayFileType

    def __repr__(self) -> str:
        return f"PlayFile(name={self.name!r}, url='<redacted>', size={self.size!r}, type={self.type!r})"


class GooglePlayAPI:
    def __init__(
        self, auth_data: AuthData, device: str = "google_pixel_9a", locale: str | Locale | None = None
    ) -> None:
        if isinstance(locale, Locale):
            self.locale = locale
        else:
            self.locale = Locale.parse(locale or default_locale() or "en_US")
        self.device = Device(device, self.locale)
        self.auth_data = auth_data
        self.client = httpx.AsyncClient(timeout=60.0, follow_redirects=True)

        if not (self.has_gsf_auth or self.has_oauth_auth or self.has_aas_auth or self.has_token_auth):
            msg = (
                "Insufficient authentication data provided to initialize API. "
                "Provide at least GSF ID and Auth Token, or Email and OAuth Login Token."
            )
            raise AuthExceptionError(msg)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.client.aclose()

    @property
    def language(self) -> str:
        return self.locale.language.lower()

    @property
    def country(self) -> str:
        return (self.locale.territory or "").lower()

    @property
    def has_gsf_auth(self) -> bool:
        return bool(self.auth_data.gsf_id and self.auth_data.auth_token)

    @property
    def has_oauth_auth(self) -> bool:
        return bool(self.auth_data.email and self.auth_data.oauth_login_token)

    @property
    def has_aas_auth(self) -> bool:
        return bool(self.auth_data.email and self.auth_data.aas_token)

    @property
    def has_token_auth(self) -> bool:
        return bool(self.auth_data.email and self.auth_data.auth_token)

    @staticmethod
    def parse_form_response(response: bytes) -> dict[str, str]:
        key_value_map: dict[str, str] = {}
        for line in response.decode().splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                key_value_map[key] = value
        return key_value_map

    @staticmethod
    def message_as_dict(message: Any) -> dict[str, Any]:
        return MessageToDict(message, always_print_fields_with_no_presence=True)

    def get_default_headers(self) -> dict[str, str]:
        if not self.auth_data.gsf_id:
            msg = "GSF ID is required to generate default headers. Try calling setup() first."
            raise AuthExceptionError(msg)

        headers: dict[str, str] = {}
        if self.auth_data.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_data.auth_token}"

        headers["User-Agent"] = self.device.user_agent_string
        headers["X-DFE-Device-Id"] = self.auth_data.gsf_id
        headers["Accept-Language"] = str(self.locale).replace("_", "-")
        headers["X-DFE-Encoded-Targets"] = DEFAULT_DFE_TARGETS
        headers["X-DFE-Phenotype"] = DEFAULT_DFE_PHENOTYPE
        headers["X-DFE-Client-Id"] = "am-android-google"
        headers["X-DFE-Network-Type"] = "4"
        headers["X-DFE-Content-Filters"] = ""
        headers["X-Limit-Ad-Tracking-Enabled"] = "false"
        headers["X-Ad-Id"] = ""
        headers["X-DFE-UserLanguages"] = self.device.user_languages
        headers["X-DFE-Request-Params"] = "timeoutMs=4000"

        if self.auth_data.device_check_in_consistency_token:
            headers["X-DFE-Device-Checkin-Consistency-Token"] = self.auth_data.device_check_in_consistency_token
        if self.auth_data.device_config_token:
            headers["X-DFE-Device-Config-Token"] = self.auth_data.device_config_token
        if self.auth_data.dfe_cookie:
            headers["X-DFE-Cookie"] = self.auth_data.dfe_cookie
        if self.device.mcc_mnc:
            headers["X-DFE-MCCMNC"] = self.device.mcc_mnc

        return headers

    def get_auth_headers(self) -> dict[str, str]:
        headers = {"app": DEFAULT_ANDROID_VENDING_PACKAGE, "User-Agent": self.device.auth_user_agent_string}
        if self.auth_data.gsf_id:
            headers["device"] = self.auth_data.gsf_id
        return headers

    def get_default_auth_params(self) -> dict[str, str]:
        if not self.auth_data.email:
            msg = "Email is required to generate default auth params. Try calling setup() first."
            raise AuthExceptionError(msg)

        params: dict[str, str] = {}
        if self.auth_data.gsf_id:
            params["androidId"] = self.auth_data.gsf_id
        params["sdk_version"] = str(self.device.sdk_version)
        params["Email"] = self.auth_data.email
        params["google_play_services_version"] = str(self.device.play_services_version)
        params["device_country"] = self.country
        params["lang"] = self.language
        params["callerSig"] = DEFAULT_CALLER_SIG
        return params

    async def _request(
        self, method: str, url: str, *, raise_for_status: bool = True, _artifact: bool = False, **request_kwargs: Any
    ) -> httpx.Response:
        route = "artifact" if _artifact else _safe_route(url)
        request_id = next(_REQUEST_IDS)
        started = perf_counter()
        context = {"http_method": method, "http_route": route, "request_id": request_id}
        logger.debug("%s %s request", method, route, extra=context)
        try:
            resp = await self.client.request(method, url, **request_kwargs)
        except httpx.RequestError as error:
            error_type = type(error).__name__
            logger.debug(
                "%s %s failed (%s)",
                method,
                route,
                error_type,
                extra={**context, "elapsed_ms": _elapsed_ms(started)},
            )
            msg = f"{method} {route} failed: {error_type}"
            raise type(error)(msg, request=error.request) from None
        except httpx.InvalidURL:
            msg = f"{method} {route} failed: invalid URL"
            raise httpx.InvalidURL(msg) from None
        logger.debug(
            "%s %s returned %s",
            method,
            route,
            resp.status_code,
            extra={
                **context,
                "http_status": resp.status_code,
                "elapsed_ms": _elapsed_ms(started),
                "response_bytes": len(resp.content),
            },
        )
        if raise_for_status:
            _raise_for_status(resp, method, route)
        return resp

    async def _play_request(self, method: str, url: str, **request_kwargs: Any) -> ResponseWrapper:
        resp = await self._request(method, url, raise_for_status=True, **request_kwargs)
        return _decode_response(ResponseWrapper, resp, method, _safe_route(url))

    async def setup(self, force: bool = False) -> None:
        logger.info("auth setup started", extra={"force": force})
        if self.auth_data.gsf_id and self.auth_data.auth_token and not force:
            logger.info("auth ready", extra={"reused": True})
            return  # Manual GSF ID and Auth Token can skip setup

        if self.auth_data.email and self.auth_data.oauth_login_token and not self.auth_data.aas_token:
            self.auth_data.aas_token = await self.generate_aas_token()  # If OAuth, get the AAS token first

        checkin_request = self.device.generate_android_checkin_request()
        checkin_response = await self.check_in(checkin_request.SerializeToString())

        self.auth_data.gsf_id = f"{checkin_response.android_id:x}"
        self.auth_data.device_check_in_consistency_token = checkin_response.device_checkin_consistency_token

        upload_device_response = await self.upload_device_config()
        self.auth_data.device_config_token = upload_device_response.upload_device_config_token

        if self.auth_data.aas_token:
            self.auth_data.auth_token = await self.generate_token(TokenService.GOOGLEPLAY)

        # https://gitlab.com/AuroraOSS/gplayapi/-/commit/735ec0e00ce51b6934a673f17c906e07373a9a43
        # Skip accepting Google ToS because it adds device to Google account
        # toc_response = await self.toc()  # noqa: ERA001
        # self.auth_data.dfe_cookie = toc_response.cookie  # noqa: ERA001

        logger.info("auth ready", extra={"reused": False})

    async def generate_aas_token(self) -> str:
        logger.debug("Requesting AAS token from OAuth login token...")
        if not self.has_oauth_auth:
            msg = "Email and OAuth login token are required to generate AAS token."
            raise AuthExceptionError(msg)

        params = self.get_default_auth_params()
        params["service"] = TokenService.AC2DM.value
        params["add_account"] = "1"
        params["get_accountid"] = "1"
        params["ACCESS_TOKEN"] = "1"
        params["callerPkg"] = DEFAULT_ANDROID_VENDING_PACKAGE
        params["Token"] = self.auth_data.oauth_login_token
        params["droidguard_results"] = "null"

        headers = self.get_auth_headers()
        headers["app"] = DEFAULT_ANDROID_VENDING_APP

        resp = await self._request("POST", URL_AUTH, headers=headers, params=params, raise_for_status=True)
        parsed = self.parse_form_response(resp.content)
        token = parsed.get("Token") or parsed.get("Auth", "")

        if not token:
            msg = "Failed to obtain AAS token"
            raise ValueError(msg)
        return token

    async def generate_token(self, service: TokenService) -> str:
        logger.debug("Generating %s token...", service.value)
        if not self.has_aas_auth:
            msg = "Email and AAS token are required to generate service tokens."
            raise AuthExceptionError(msg)

        headers = self.get_auth_headers()
        params = self.get_default_auth_params()
        params["app"] = DEFAULT_ANDROID_VENDING_APP
        params["client_sig"] = DEFAULT_CLIENT_SIG
        params["callerPkg"] = DEFAULT_ANDROID_VENDING_PACKAGE
        params["Token"] = self.auth_data.aas_token
        params["oauth2_foreground"] = "1"
        params["token_request_options"] = "CAA4AVAB"
        params["check_email"] = "1"
        params["system_partition"] = "1"
        params["droidguard_results"] = "null"

        match service:
            case TokenService.AC2DM:
                params["service"] = TokenService.AC2DM
                params.pop("app", None)
            case TokenService.ANDROID_CHECK_IN_SERVER:
                params["oauth2_foreground"] = "0"
                params["app"] = DEFAULT_ANDROID_VENDING_PACKAGE
                params["service"] = TokenService.ANDROID_CHECK_IN_SERVER
            case TokenService.OAUTHLOGIN:
                params["oauth2_foreground"] = "0"
                params["app"] = "com.google.android.googlequicksearchbox"
                params["service"] = f"oauth2:https://www.google.com/accounts/{TokenService.OAUTHLOGIN}"
                params["callerPkg"] = "com.google.android.googlequicksearchbox"
            case TokenService.EXPERIMENTAL_CONFIG:
                params["service"] = f"oauth2:https://www.googleapis.com/auth/{TokenService.EXPERIMENTAL_CONFIG}"
            case TokenService.NUMBERER | TokenService.GCM:
                params["app"] = DEFAULT_ANDROID_VENDING_PACKAGE
                params["service"] = f"oauth2:https://www.googleapis.com/auth/{service}"
            case TokenService.GOOGLEPLAY:
                params["service"] = f"oauth2:https://www.googleapis.com/auth/{service}"
            case TokenService.ANDROID:
                params["service"] = TokenService.ANDROID

        resp = await self._request("POST", URL_AUTH, headers=headers, params=params, raise_for_status=True)
        parsed = self.parse_form_response(resp.content)
        auth = parsed.get("Auth", "")
        if not auth:
            msg = f"Failed to obtain {service.value} token"
            raise AuthExceptionError(msg)
        return auth

    async def check_in(self, request: bytes) -> AndroidCheckinResponse:
        logger.debug("Performing device check-in...")
        headers = self.get_auth_headers()
        headers["Content-Type"] = "application/x-protobuffer"
        headers["Host"] = "android.clients.google.com"
        resp = await self._request("POST", URL_CHECK_IN, headers=headers, content=request)
        return _decode_response(AndroidCheckinResponse, resp, "POST", _safe_route(URL_CHECK_IN))

    async def upload_device_config(self) -> UploadDeviceConfigResponse:
        logger.debug("Uploading device configuration...")
        headers = self.get_default_headers()
        headers["Content-Type"] = "application/x-protobuf"
        request = UploadDeviceConfigRequest(device_configuration=self.device.device_configuration).SerializeToString()
        resp = await self._play_request("POST", URL_UPLOAD_DEVICE_CONFIG, headers=headers, content=request)
        return resp.payload.upload_device_config_response

    async def toc(self) -> TocResponse:
        logger.debug("Checking Terms of Service...")
        headers = self.get_default_headers()
        res = await self._play_request("GET", URL_TOC, headers=headers)
        toc = res.payload.toc_response
        if toc.tos_content and toc.tos_token:
            await self.accept_tos(toc.tos_token)
        return toc

    async def accept_tos(self, tos_token: str) -> AcceptTosResponse:
        logger.debug("Accepting Terms of Service...")
        headers = self.get_default_headers()
        params = {"tost": tos_token, "toscme": "false"}
        resp = await self._play_request("POST", URL_TOS_ACCEPT, headers=headers, params=params)
        return resp.payload.accept_tos_response

    async def get_user_profile(self) -> UserProfile | None:
        headers = self.get_default_headers()
        resp = await self._request("GET", URL_USER_PROFILE, headers=headers, raise_for_status=False)
        if resp.status_code == httpx.codes.NOT_FOUND:
            return None
        route = _safe_route(URL_USER_PROFILE)
        _raise_for_status(resp, "GET", route)
        return _decode_response(ResponseWrapperApi, resp, "GET", route).payload.user_profile_response.user_profile

    async def get_app_details_by_package_name(self, package_name: str) -> DetailsResponse:
        headers = self.get_default_headers()
        params = {"doc": package_name}
        resp = await self._play_request("GET", URL_DETAILS, headers=headers, params=params)
        return resp.payload.details_response

    async def get_bulk_app_details_by_package_names(self, package_names: list[str]) -> list[BulkDetailsEntry]:
        headers = self.get_default_headers()
        headers["Content-Type"] = "application/x-protobuf"
        request = BulkDetailsRequest(doc_id=package_names).SerializeToString()
        resp = await self._play_request("POST", URL_BULK_DETAILS, headers=headers, content=request)
        return list(resp.payload.bulk_details_response.entry)

    async def get_dev_stream(self, dev_id: str) -> ListResponse:
        headers = self.get_default_headers()
        url = f"{URL_FDFE}/getDeveloperPageStream"
        resp = await self._play_request("GET", url, headers=headers, params={"docid": f"developer-{dev_id}"})
        return _stream_list_response(resp)

    async def get_stream_tree_response(self, stream_or_next_url: str) -> StreamResponse:
        """Read items and their node tree from a stream or pagination URL."""
        headers = self.get_default_headers()
        url = _fdfe_url(stream_or_next_url)
        response = await self._request("GET", url, headers=headers)
        return _decode_response(StreamResponse, response, "GET", _safe_route(url))

    async def get_testing_program_details(
        self, package_name: str, *, subscribe: bool = False
    ) -> TestingProgramResponse:
        headers = self.get_default_headers()
        request = TestingProgramRequest(package_name=package_name, subscribe=subscribe).SerializeToString()
        resp = await self._play_request("POST", URL_TESTING_PROGRAM, headers=headers, content=request)
        return resp.payload.testing_program_response

    async def get_all_categories(self, category_type: CategoryType) -> Item:
        headers = self.get_default_headers()
        headers["User-Agent"] = LEGACY_USER_AGENT
        params = {"c": "3", "cat": category_type}
        resp = await self._play_request("GET", URL_CATEGORIES, headers=headers, params=params)
        return resp.payload.list_response.item

    async def get_category_stream(self, stream_or_next_url: str) -> ListResponse:
        headers = self.get_default_headers()
        url = _fdfe_url(stream_or_next_url)
        resp = await self._play_request("GET", url, headers=headers)
        return _stream_list_response(resp)

    async def get_my_apps(self, cluster_type: MyAppsClusterType) -> ListResponse:
        headers = self.get_default_headers()
        params = {"n": "15", "tab": cluster_type}
        url = f"{URL_FDFE}/myAppsStream"
        resp = await self._play_request("GET", url, headers=headers, params=params)
        return _stream_list_response(resp)

    async def get_next_stream_response(self, next_url: str) -> ListResponse:
        headers = self.get_default_headers()
        url = _fdfe_url(next_url)
        resp = await self._play_request("GET", url, headers=headers)
        return _stream_list_response(resp)

    async def get_browse_response(self, browse_url: str) -> BrowseResponse:
        headers = self.get_default_headers()
        url = _fdfe_url(browse_url)
        resp = await self._play_request("GET", url, headers=headers)
        return resp.payload.browse_response

    async def get_wishlist_apps(self) -> ListResponse:
        headers = self.get_default_headers()
        params = {"c": "0", "dt": "7", "libid": "u-wl"}
        resp = await self._play_request("GET", URL_LIBRARY, headers=headers, params=params)
        return resp.payload.list_response

    async def modify_wishlist(self, action: Literal["add", "remove"], package_names: list[str]) -> bool:
        headers = self.get_default_headers()
        if action == "add":
            req = ModifyLibraryRequest(library_id="u-wl", add_package_name=package_names).SerializeToString()
        elif action == "remove":
            req = ModifyLibraryRequest(library_id="u-wl", remove_package_name=package_names).SerializeToString()
        resp = await self._request("POST", URL_MODIFY_LIBRARY, headers=headers, content=req)
        return resp.is_success

    async def get_reviews(
        self, package_name: str, review_filter: ReviewFilter = ReviewFilter.ALL, result_num: int = 20
    ) -> ReviewResponse:
        headers = self.get_default_headers()
        params = {"doc": package_name, "n": str(result_num)}

        if review_filter == ReviewFilter.NEWEST:
            params["sort"] = review_filter
        elif review_filter == ReviewFilter.ALL:
            params["sfilter"] = review_filter
        elif review_filter in [ReviewFilter.POSITIVE, ReviewFilter.CRITICAL]:
            params["sent"] = review_filter
        else:
            params["rating"] = review_filter

        resp = await self._play_request("GET", URL_REVIEWS, headers=headers, params=params)
        return resp.payload.review_response

    async def get_review_summary(self, package_name: str) -> ReviewResponse:
        headers = self.get_default_headers()
        params = {"doc": package_name}
        url = f"{URL_FDFE}/reviewSummary"
        resp = await self._play_request("GET", url, headers=headers, params=params)
        return resp.payload.review_summary_response

    async def get_user_review(self, package_name: str, testing: bool = False) -> Review | None:
        headers = self.get_default_headers()
        params = {"doc": package_name, "itpr": str(testing).lower()}
        resp = await self._play_request("GET", URL_REVIEW_USER, headers=headers, params=params)
        if review := resp.payload.review_response.user_reviews_response.review:
            return review[0]
        return None

    async def add_or_edit_review(
        self, package_name: str, title: str, content: str, rating: int, is_beta: bool = False
    ) -> Review:
        headers = self.get_default_headers()
        params = {
            "doc": package_name,
            "title": title,
            "content": content,
            "rating": str(rating),
            "rst": "3",
            "itpr": str(is_beta).lower(),
        }
        resp = await self._play_request("POST", URL_REVIEW_ADD_EDIT, headers=headers, params=params)
        review_response = resp.payload.review_response
        if review_response.HasField("user_review"):
            return review_response.user_review
        msg = "No review returned by addReview"
        raise ValueError(msg)

    async def delete_review(self, package_name: str, is_beta: bool = False) -> bool:
        headers = self.get_default_headers()
        params = {"doc": package_name, "itpr": str(is_beta).lower()}
        resp = await self._request("POST", URL_REVIEW_DELETE, headers=headers, params=params)
        return resp.is_success

    async def get_next_reviews(self, next_page_url: str) -> ReviewResponse:
        headers = self.get_default_headers()
        url = _fdfe_url(next_page_url)
        resp = await self._play_request("GET", url, headers=headers)
        return resp.payload.review_response

    async def search_suggestions(self, query: str) -> SearchSuggestResponse:
        headers = self.get_default_headers()
        headers["User-Agent"] = LEGACY_USER_AGENT
        params = [("q", query), ("sb", "5"), ("sst", "2"), ("sst", "3")]
        resp = await self._play_request("GET", URL_SEARCH_SUGGEST, headers=headers, params=params)
        return resp.payload.search_suggest_response

    async def search_results(self, query: str, next_page_url: str = "") -> ListResponse:
        headers = self.get_default_headers()
        if next_page_url:
            resp = await self._play_request("GET", _fdfe_url(next_page_url), headers=headers)
        else:
            params = {"q": query, "c": "3", "ksm": "1"}
            resp = await self._play_request("GET", URL_SEARCH, headers=headers, params=params)
        return _stream_list_response(resp)

    async def get_list_response(self, stream_type: StreamType, category: StreamCategory | None = None) -> ListResponse:
        headers = self.get_default_headers()
        params = {"c": "3"}

        if stream_type == StreamType.EARLY_ACCESS:
            params["ct"] = "1"
        elif category and category != StreamCategory.NONE:
            params["cat"] = category

        url = str(httpx.URL(_fdfe_url(stream_type)).copy_merge_params(params))
        resp = await self._play_request("GET", url, headers=headers)
        return _stream_list_response(resp)

    async def get_cluster(self, category: str, chart: str) -> ListResponse | None:
        headers = self.get_default_headers()
        headers["User-Agent"] = LEGACY_USER_AGENT
        params = {"c": "3", "stcid": chart, "scat": category}
        try:
            resp = await self._play_request("GET", URL_TOP_CHART, headers=headers, params=params)
        except httpx.HTTPStatusError as error:
            if error.response.status_code == httpx.codes.NOT_FOUND:
                return None
            raise
        return _stream_list_response(resp)

    async def get_purchase_history(self, offset: int = 0) -> ListResponse:
        headers = self.get_default_headers()
        params = {"o": str(offset)}
        resp = await self._play_request("GET", URL_PURCHASE_HISTORY, headers=headers, params=params)
        return resp.payload.list_response

    async def get_delivery_token(
        self, package_name: str, version_code: int, offer_type: int, certificate_hash: str | None = None
    ) -> str:
        headers = self.get_default_headers()
        params = {"ot": str(offer_type), "doc": package_name, "vc": str(version_code)}
        if certificate_hash:
            params["ch"] = certificate_hash
        try:
            resp = await self._play_request("POST", URL_PURCHASE, headers=headers, params=params)
        except httpx.HTTPStatusError as error:
            if error.response.status_code == httpx.codes.BAD_REQUEST:
                return ""
            raise
        return resp.payload.buy_response.encoded_delivery_token

    async def get_delivery_response(
        self,
        package_name: str,
        update_version_code: int,
        offer_type: int,
        split_module: str | None = None,
        installed_version_code: int | None = None,
        patch_format: PatchFormat = PatchFormat.GZIPPED_BSDIFF,
        delivery_token: str = "",
        certificate_hash: str | None = None,
        *,
        installed_derived_apk_id: int | None = None,
        installed_frosting_id: int | None = None,
        patch_formats: Sequence[PatchFormat] | None = None,
    ) -> DeliveryResponse:
        headers = self.get_default_headers()
        params = {"ot": str(offer_type), "doc": package_name, "vc": str(update_version_code)}
        requested_formats: list[tuple[str, str]] = []

        if installed_version_code and installed_version_code > 0:
            params["bvc"] = str(installed_version_code)
            formats = [patch_format] if patch_formats is None else patch_formats
            requested_formats = [("pf", str(format_.value)) for format_ in dict.fromkeys(formats)]
            if installed_derived_apk_id:
                params["bda"] = str(installed_derived_apk_id)
            if installed_frosting_id:
                params["bf"] = str(installed_frosting_id)

        if split_module:
            params["mn"] = split_module
        if certificate_hash:
            params["ch"] = certificate_hash
        if delivery_token:
            params["dtok"] = delivery_token

        resp = await self._play_request(
            "GET", URL_DELIVERY, headers=headers, params=[*params.items(), *requested_formats]
        )
        return resp.payload.delivery_response

    async def acquire(self, package_name: str, version_code: int, offer_type: int) -> AcquireResponseWrapper:
        acquire_request = AcquireRequest(
            package=AcquireRequest.Package(
                payload=AcquireRequest.Package.Payload(f2=1, f3=3, package_name=package_name), f2=1
            ),
            version=AcquireRequest.Version(version_code=version_code, f3=0),
            f15=0,
            f8=None,
            offer_type=offer_type,
            nonce=f"nonce={base64.urlsafe_b64encode(secrets.token_bytes(256)).rstrip(b'=').decode('utf-8')}",
            f25=2,
            m30=AcquireRequest.Message30(f1=2, f2=0),
        )
        body = acquire_request.SerializeToString()
        headers = self.get_default_headers()
        resp = await self._request("POST", URL_ACQUIRE, headers=headers, content=body)
        return _decode_response(AcquireResponseWrapper, resp, "POST", _safe_route(URL_ACQUIRE))

    async def purchase(
        self,
        package_name: str,
        version_code: int,
        offer_type: int,
        certificate_hash: str | None = None,
        split_module: str | None = None,
        installed_version_code: int | None = None,
        patch_format: PatchFormat = PatchFormat.GZIPPED_BSDIFF,
        *,
        installed_derived_apk_id: int | None = None,
        installed_frosting_id: int | None = None,
        patch_formats: Sequence[PatchFormat] | None = None,
    ) -> DeliveryResponse:
        # https://gitlab.com/AuroraOSS/gplayapi/-/commit/2180d4a50efac9b86f83e2bfb84db3366d41476d
        # It doesn't matter if this fails
        try:
            await self.acquire(package_name, version_code, offer_type)
        except Exception as error:
            logger.debug(
                "acquire failed; continuing for %r",
                package_name,
                extra={"version_code": version_code, "offer_type": offer_type, "error_type": type(error).__name__},
            )

        delivery_token = await self.get_delivery_token(package_name, version_code, offer_type, certificate_hash)
        delivery_response = await self.get_delivery_response(
            package_name=package_name,
            update_version_code=version_code,
            offer_type=offer_type,
            delivery_token=delivery_token,
            certificate_hash=certificate_hash,
            split_module=split_module,
            installed_version_code=installed_version_code,
            patch_format=patch_format,
            installed_derived_apk_id=installed_derived_apk_id,
            installed_frosting_id=installed_frosting_id,
            patch_formats=patch_formats,
        )

        if delivery_response.status == DeliveryResponseStatus.SUCCESS:
            if not self.parse_delivery_response(package_name, delivery_response, version_code=version_code):
                raise EmptyDownloadsError
            logger.debug(
                "purchase complete for %r",
                package_name,
                extra={"version_code": version_code, "offer_type": offer_type, "status": delivery_response.status},
            )
            return delivery_response
        if delivery_response.status in [
            DeliveryResponseStatus.NOT_SUPPORTED_FOR_PURCHASE,
            DeliveryResponseStatus.NOT_SUPPORTED_FOR_PURCHASE_2,
        ]:
            msg = f"App {package_name}-{version_code} is not purchasable."
            raise PurchaseError(msg)
        if delivery_response.status == DeliveryResponseStatus.NOT_PURCHASED:
            msg = f"App {package_name}-{version_code} is not purchased."
            raise PurchaseError(msg)
        if delivery_response.status == DeliveryResponseStatus.REMOVED_FROM_STORE:
            msg = f"App {package_name}-{version_code} has been removed from the store."
            raise PurchaseError(msg)
        msg = f"Unknown error purchasing app {package_name}-{version_code}. Status: {delivery_response.status}"
        raise PurchaseError(msg)

    async def download_app(
        self,
        package_name: str,
        output_dir: Path,
        version_code: int | None = None,
        offer_type: int | None = None,
        certificate_hash: str | None = None,
        split_module: str | None = None,
        installed_version_code: int | None = None,
        patch_format: PatchFormat = PatchFormat.GZIPPED_BSDIFF,
        use_xapk: bool = True,
        custom_apk_name: str | None = None,
        include_dex: bool = False,
        *,
        installed_derived_apk_id: int | None = None,
        installed_frosting_id: int | None = None,
        patch_formats: Sequence[PatchFormat] | None = None,
    ) -> None:
        started = perf_counter()
        logger.info("download started for %r", package_name)
        if output_dir.is_file():
            msg = f"Output directory {output_dir} is a file. Please provide a valid directory path."
            raise ValueError(msg)
        output_dir.mkdir(parents=True, exist_ok=True)

        details = await self.get_app_details_by_package_name(package_name)
        vc = version_code or details.item.details.app_details.version_code
        ot = offer_type or details.item.offer[0].offer_type

        delivery_response = await self.purchase(
            package_name=package_name,
            version_code=vc,
            offer_type=ot,
            certificate_hash=certificate_hash,
            split_module=split_module,
            installed_version_code=installed_version_code,
            patch_format=patch_format,
            installed_derived_apk_id=installed_derived_apk_id,
            installed_frosting_id=installed_frosting_id,
            patch_formats=patch_formats,
        )

        files = self.parse_delivery_response(package_name, delivery_response, version_code=vc)
        if not files:
            raise EmptyDownloadsError
        downloaded_bytes = 0
        file_count = 0
        if len(files) == 1:
            output_path = output_dir / (custom_apk_name or files[0].name)
            downloaded_bytes += await self._save_play_file(files[0], output_path)
            file_count += 1
        else:
            for file in files:
                if file.type == PlayFileType.DEX and not include_dex:
                    continue
                output_path = output_dir / file.name
                downloaded_bytes += await self._save_play_file(file, output_path)
                file_count += 1

        if use_xapk and len(files) > 1:
            self.make_xapk(
                details.item.details.app_details.package_name,
                details,
                files,
                output_dir,
                custom_apk_name,
                include_dex,
            )
        logger.info(
            "download complete for %r",
            package_name,
            extra={
                "version_code": vc,
                "offer_type": ot,
                "file_count": file_count,
                "downloaded_bytes": downloaded_bytes,
                "elapsed_ms": _elapsed_ms(started),
            },
        )

    async def _save_play_file(self, file: PlayFile, output_path: Path) -> int:
        response = await self._request("GET", file.url, _artifact=True)
        actual_size = len(response.content)
        if file.size < 0:
            msg = f"Invalid download size: {file.size}"
            raise ValueError(msg)
        if actual_size != file.size:
            msg = f"Download size mismatch: expected {file.size} bytes, got {actual_size}"
            raise ValueError(msg)
        output_path.write_bytes(response.content)
        logger.debug(
            "file download complete",
            extra={"file_type": file.type.value, "byte_count": actual_size, "expected_bytes": file.size},
        )
        return actual_size

    def make_xapk(
        self,
        package_name: str,
        details: DetailsResponse,
        files: list[PlayFile],
        output_dir: Path,
        custom_apk_name: str | None = None,
        include_dex: bool = False,
    ) -> None:
        manifest = self.make_xapk_manifest(details, files, include_dex=include_dex)
        manifest_path = output_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=4, ensure_ascii=False))
        base_file = next((file for file in files if file.type == PlayFileType.BASE), None)

        with ZipFile(output_dir / f"{custom_apk_name or package_name}.xapk", "w") as zipf:
            for file in files:
                if file.type == PlayFileType.DEX and not include_dex:
                    continue
                zipf.write(output_dir / file.name, arcname=file.name)
            if base_file is not None and (
                icon_data := self.extract_icon_from_apk((output_dir / base_file.name).read_bytes())
            ):
                manifest["icon"] = "icon.png"
                manifest_path.write_text(json.dumps(manifest, indent=4, ensure_ascii=False))
                zipf.writestr("icon.png", icon_data)
            zipf.write(manifest_path, arcname="manifest.json")

        cleanup_failures = 0
        cleanup_paths = [output_dir / file.name for file in files if include_dex or file.type != PlayFileType.DEX]
        for path in [*cleanup_paths, manifest_path]:
            try:
                path.unlink(missing_ok=True)
            except OSError:
                cleanup_failures += 1
        if cleanup_failures:
            logger.warning("xapk cleanup incomplete", extra={"cleanup_failures": cleanup_failures})
        logger.debug("xapk created", extra={"input_file_count": len(cleanup_paths)})

    @staticmethod
    def extract_icon_from_apk(apk_data: bytes) -> bytes | None:
        icon_paths = [
            "res/mipmap-xxxhdpi-v4/app_icon.png",
            "res/mipmap-xxhdpi-v4/app_icon.png",
            "res/mipmap-xhdpi-v4/app_icon.png",
            "res/mipmap-hdpi-v4/app_icon.png",
            "res/mipmap-mdpi-v4/app_icon.png",
            "res/mipmap-ldpi-v4/app_icon.png",
        ]

        with ZipFile(BytesIO(apk_data)) as apk:
            for icon_path in icon_paths:
                try:
                    with apk.open(icon_path) as icon_file:
                        return icon_file.read()
                except KeyError:
                    continue
        return None

    @staticmethod
    def make_xapk_manifest(
        app_details: DetailsResponse, files: list[PlayFile], include_dex: bool = False
    ) -> dict[str, Any]:
        details = app_details.item.details.app_details
        manifest: dict[str, Any] = {
            "xapk_version": "2",
            "package_name": details.package_name,
            "name": app_details.item.title,
            "locales_name": {},
            "version_code": str(details.version_code),
            "version_name": details.version_string,
            "min_sdk_version": "24",
            "target_sdk_version": str(details.target_sdk_version),
            "permissions": list(details.permission),
            "total_size": 0,
            "split_apks": [],
            "expansions": [],
        }
        for file in files:
            if file.type == PlayFileType.BASE:
                manifest["total_size"] += file.size
                manifest["split_apks"].append({"file": file.name, "id": "base"})
            elif file.type in [PlayFileType.OBB, PlayFileType.PATCH]:
                manifest["total_size"] += file.size
                manifest["expansions"].append(
                    {
                        "file": file.name,
                        "install_location": "EXTERNAL_STORAGE",
                        "install_path": f"Android/obb/{details.package_name}/{file.name}",
                    }
                )
            elif file.type == PlayFileType.SPLIT:
                manifest["total_size"] += file.size
                manifest["split_apks"].append({"file": file.name, "id": file.name.replace(".apk", "")})
            # I don't think XAPK manifest has a standard way to include DEX files?
            # https://openxapkfile.net/manifest.html
            elif file.type == PlayFileType.DEX and include_dex:
                logger.warning("dex file omitted from xapk manifest")
        return manifest

    def parse_delivery_response(
        self, package_name: str, response: DeliveryResponse, version_code: int = 0
    ) -> list[PlayFile]:
        delivery_data = response.app_delivery_data

        files: list[PlayFile] = []
        if delivery_data.download_url.strip():
            files.append(
                PlayFile(
                    name="base.apk",
                    url=delivery_data.download_url,
                    size=delivery_data.download_size,
                    type=PlayFileType.BASE,
                )
            )
        for additional_file in delivery_data.additional_file:
            if not additional_file.download_url.strip():
                continue
            is_obb = additional_file.file_type == 0
            file_type = "main" if is_obb else "patch"
            obb_version_code = additional_file.version_code or version_code
            files.append(
                PlayFile(
                    name=f"{file_type}.{obb_version_code}.{package_name}.obb",
                    url=additional_file.download_url,
                    size=additional_file.download_size,
                    type=PlayFileType.OBB if is_obb else PlayFileType.PATCH,
                )
            )
        for split in delivery_data.split_delivery_data:
            if not split.download_url.strip():
                continue
            files.append(
                PlayFile(
                    name=f"{split.name}.apk",
                    url=split.download_url,
                    size=split.download_size,
                    type=PlayFileType.SPLIT,
                )
            )
            if split.HasField("dex_metadata") and split.dex_metadata.download_url.strip():
                files.append(
                    PlayFile(
                        name=f"{split.name}.dm",
                        url=split.dex_metadata.download_url,
                        size=split.dex_metadata.download_size,
                        type=PlayFileType.DEX,
                    )
                )

        if delivery_data.HasField("dex_metadata") and delivery_data.dex_metadata.download_url.strip():
            files.append(
                PlayFile(
                    name="base.dm",
                    url=delivery_data.dex_metadata.download_url,
                    size=delivery_data.dex_metadata.download_size,
                    type=PlayFileType.DEX,
                )
            )

        return files if any(file.type != PlayFileType.DEX for file in files) else []
