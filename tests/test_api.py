# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import AsyncMock, patch
from zipfile import ZipFile

import httpx

from pyplay import AuthData, EmptyDownloadsError, GooglePlayAPI
from pyplay.constants import CategoryType, MyAppsClusterType, PatchFormat, PlayFileType, StreamType, TokenService
from pyplay.playprotos.google_play import AndroidCheckinResponse, DeliveryResponse, DetailsResponse, ResponseWrapper
from pyplay.playprotos.stream import StreamResponse


class APIRequestTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.api = GooglePlayAPI(AuthData(gsf_id="test-device", auth_token="test-auth"), locale="en_US")
        await self.api.client.aclose()
        self.body = b""
        self.status = 200
        self.requests: list[httpx.Request] = []

        def respond(request: httpx.Request) -> httpx.Response:
            self.requests.append(request)
            return httpx.Response(self.status, content=self.body)

        self.api.client = httpx.AsyncClient(transport=httpx.MockTransport(respond))
        self.addAsyncCleanup(self.api.client.aclose)

    async def test_list_streams_read_prefetched_payloads(self) -> None:
        response = ResponseWrapper()
        response.payload.list_response.item.title = "top-level stub"
        response.pre_fetch.response.payload.list_response.item.title = "prefetched items"
        self.body = response.SerializeToString()
        calls = [
            lambda: self.api.get_dev_stream("example"),
            lambda: self.api.get_category_stream("browse?category=tools"),
            lambda: self.api.get_my_apps(MyAppsClusterType.MY_APPS_LIBRARY),
            lambda: self.api.get_next_stream_response("browse?ptkn=next"),
            lambda: self.api.get_list_response(StreamType.TOP_CHART),
            lambda: self.api.get_cluster("APPLICATION", "topselling_free"),
            lambda: self.api.search_results("browser"),
        ]
        for call in calls:
            with self.subTest(call=call):
                result = await call()
                self.assertEqual(result.item.title, "prefetched items")

    async def test_streams_use_top_level_payload_when_prefetch_is_absent(self) -> None:
        response = ResponseWrapper()
        response.payload.list_response.item.title = "ordinary items"
        self.body = response.SerializeToString()
        result = await self.api.search_results("browser")
        self.assertEqual(result.item.title, "ordinary items")

    async def test_categories_keep_their_own_top_level_payload(self) -> None:
        response = ResponseWrapper()
        response.payload.list_response.item.title = "categories"
        response.pre_fetch.response.payload.list_response.item.title = "unrelated prefetch"
        self.body = response.SerializeToString()
        result = await self.api.get_all_categories(CategoryType.APPLICATION)
        self.assertEqual(result.title, "categories")

    async def test_search_suggestions_repeat_sst_and_encode_the_query(self) -> None:
        query = "a&b=c d#e"
        await self.api.search_suggestions(query)
        request = self.requests[-1]
        self.assertEqual(request.url.params["q"], query)
        self.assertEqual(request.url.params.get_list("sst"), ["2", "3"])
        self.assertNotIn("sdt", request.url.params)

    async def test_search_cursor_is_requested_without_rewriting_its_query(self) -> None:
        await self.api.search_results("unused", "search?ptkn=a%2Bb&q=original&c=7")
        self.assertEqual(self.requests[-1].url.query, b"ptkn=a%2Bb&q=original&c=7")

    async def test_library_nav_stream_preserves_its_tab(self) -> None:
        await self.api.get_list_response(StreamType.MY_APPS_LIBRARY)
        self.assertEqual(self.requests[-1].url.path, "/fdfe/myAppsStream")
        self.assertEqual(self.requests[-1].url.params["tab"], "LIBRARY")
        self.assertEqual(self.requests[-1].url.params["c"], "3")

    async def test_developer_id_is_encoded_as_a_single_query_parameter(self) -> None:
        await self.api.get_dev_stream("developer&id=42#fragment")
        self.assertEqual(self.requests[-1].url.params["docid"], "developer-developer&id=42#fragment")
        self.assertEqual(len(self.requests[-1].url.params), 1)

    async def test_add_review_reads_the_singular_user_review_field(self) -> None:
        response = ResponseWrapper()
        response.payload.review_response.user_review.title = "Great app"
        self.body = response.SerializeToString()
        review = await self.api.add_or_edit_review("example.app", "Great app", "A&B", 5, is_beta=True)
        self.assertEqual(review.title, "Great app")
        request = self.requests[-1]
        self.assertEqual(request.url.path, "/fdfe/addReview")
        self.assertEqual(request.content, b"")
        self.assertEqual(request.url.params["content"], "A&B")
        self.assertEqual(request.url.params["itpr"], "true")

    async def test_delete_and_user_review_encode_lowercase_beta_flags(self) -> None:
        await self.api.delete_review("example.app", is_beta=True)
        self.assertEqual(self.requests[-1].url.params["itpr"], "true")
        self.assertEqual(self.requests[-1].content, b"")
        await self.api.get_user_review("example.app", testing=False)
        self.assertEqual(self.requests[-1].url.params["itpr"], "false")

    async def test_purchase_400_allows_a_delivery_without_a_token(self) -> None:
        self.status = 400
        self.assertEqual(await self.api.get_delivery_token("example.app", 42, 1), "")
        self.status = 200
        await self.api.get_delivery_response("example.app", 42, 1, delivery_token="")
        self.assertNotIn("dtok", self.requests[-1].url.params)

    async def test_paid_app_purchase_reaches_delivery_after_purchase_400(self) -> None:
        response = ResponseWrapper()
        response.payload.delivery_response.status = 1
        response.payload.delivery_response.app_delivery_data.download_url = "https://example.invalid/base.apk"
        await self.api.client.aclose()

        def respond(request: httpx.Request) -> httpx.Response:
            self.requests.append(request)
            if request.url.path == "/fdfe/purchase":
                return httpx.Response(400)
            return httpx.Response(200, content=response.SerializeToString())

        self.api.client = httpx.AsyncClient(transport=httpx.MockTransport(respond))
        self.addAsyncCleanup(self.api.client.aclose)
        delivery = await self.api.purchase("example.app", 42, 1)
        self.assertEqual(delivery.status, 1)
        self.assertEqual(
            [request.url.path for request in self.requests], ["/fdfe/acquire", "/fdfe/purchase", "/fdfe/delivery"]
        )
        self.assertNotIn("dtok", self.requests[-1].url.params)

    async def test_successful_purchase_with_no_files_is_rejected(self) -> None:
        with (
            patch.object(self.api, "acquire", AsyncMock()),
            patch.object(self.api, "get_delivery_token", AsyncMock(return_value="")),
            patch.object(self.api, "get_delivery_response", AsyncMock(return_value=DeliveryResponse(status=1))),
            self.assertRaises(EmptyDownloadsError),
        ):
            await self.api.purchase("example.app", 42, 1)

    async def test_purchase_other_status_errors_still_propagate(self) -> None:
        for status in (401, 403, 429, 500):
            with self.subTest(status=status):
                self.status = status
                with self.assertRaises(httpx.HTTPStatusError) as caught:
                    await self.api.get_delivery_token("example.app", 42, 1)
                self.assertEqual(caught.exception.response.status_code, status)

    async def test_patch_request_describes_the_installed_base(self) -> None:
        await self.api.get_delivery_response(
            "example.app",
            42,
            1,
            installed_version_code=40,
            patch_format=PatchFormat.GZIPPED_BSDIFF,
            installed_derived_apk_id=5,
            installed_frosting_id=1234,
        )
        query = self.requests[-1].url.params
        self.assertEqual(query["bvc"], "40")
        self.assertEqual(query["pf"], "3")
        self.assertEqual(query["bda"], "5")
        self.assertEqual(query["bf"], "1234")

    async def test_patch_fields_are_omitted_without_a_positive_installed_version(self) -> None:
        for version in (None, 0, -1):
            with self.subTest(version=version):
                await self.api.get_delivery_response(
                    "example.app",
                    42,
                    1,
                    installed_version_code=version,
                    installed_derived_apk_id=5,
                    installed_frosting_id=1234,
                )
                for key in ("bvc", "pf", "bda", "bf"):
                    self.assertNotIn(key, self.requests[-1].url.params)

    async def test_patch_formats_are_repeated_once_per_distinct_format(self) -> None:
        await self.api.get_delivery_response(
            "example.app",
            42,
            1,
            installed_version_code=40,
            patch_formats=[PatchFormat.GZIPPED_BSDIFF, PatchFormat.BROTLI_FILEBYFILE, PatchFormat.GZIPPED_BSDIFF],
        )
        self.assertEqual(self.requests[-1].url.params.get_list("pf"), ["3", "5"])
        await self.api.get_delivery_response("example.app", 42, 1, installed_version_code=40, patch_formats=[])
        self.assertNotIn("pf", self.requests[-1].url.params)

    async def test_missing_chart_is_none_and_other_failures_propagate(self) -> None:
        self.status = 404
        self.assertIsNone(await self.api.get_cluster("APPLICATION", "topselling_free"))
        for status in (400, 401, 403, 429, 500):
            with self.subTest(status=status):
                self.status = status
                with self.assertRaises(httpx.HTTPStatusError):
                    await self.api.get_cluster("APPLICATION", "topselling_free")

    async def test_aas_exchange_accepts_an_auth_response_field(self) -> None:
        self.api.auth_data.email = "example@example.invalid"
        self.api.auth_data.oauth_login_token = "test-oauth"
        self.body = b"Auth=generated-aas-token"
        self.assertEqual(await self.api.generate_aas_token(), "generated-aas-token")

    async def test_googleplay_token_uses_the_vending_app(self) -> None:
        self.api.auth_data.email = "example@example.invalid"
        self.api.auth_data.aas_token = "test-aas"
        self.body = b"Auth=generated-auth-token"
        await self.api.generate_token(TokenService.GOOGLEPLAY)
        self.assertEqual(self.requests[-1].url.params["app"], "com.android.vending")
        self.assertEqual(self.requests[-1].headers["app"], "com.google.android.gms")
        self.assertEqual(self.requests[-1].content, b"")

    async def test_checkin_uses_the_protobuffer_media_type(self) -> None:
        self.body = AndroidCheckinResponse().SerializeToString()
        await self.api.check_in(b"request")
        self.assertEqual(self.requests[-1].headers["Content-Type"], "application/x-protobuffer")

    async def test_stream_tree_response_preserves_items_nodes_and_cursor(self) -> None:
        response = StreamResponse()
        response.item.add().metadata.package_name.data = "example.app"
        page = response.tree.page.add()
        page.key.url = "getHomeStream?c=3"
        page.content.children.next_page_token = "continue"
        response.tree.node.add().key.id = "item-node"
        self.body = response.SerializeToString()
        result = await self.api.get_stream_tree_response("getHomeStream?c=3")
        self.assertEqual(result, response)
        self.assertEqual(self.requests[-1].url.path, "/fdfe/getHomeStream")

    async def test_stream_cursor_supports_relative_and_same_origin_absolute_urls(self) -> None:
        for cursor in (
            "browse?ptkn=next",
            "/fdfe/browse?ptkn=next",
            "https://android.clients.google.com/fdfe/browse?ptkn=next",
        ):
            with self.subTest(cursor=cursor):
                await self.api.get_next_stream_response(cursor)
                self.assertEqual(self.requests[-1].url.path, "/fdfe/browse")
                self.assertEqual(self.requests[-1].url.params["ptkn"], "next")

    async def test_stream_cursor_rejects_an_unrelated_origin(self) -> None:
        with self.assertRaises(ValueError):
            await self.api.get_next_stream_response("https://example.invalid/steal-auth")
        self.assertEqual(self.requests, [])

    async def test_empty_delivery_fails_before_any_file_request(self) -> None:
        details = DetailsResponse()
        details.item.details.app_details.version_code = 42
        details.item.offer.add(offer_type=1)
        with (
            TemporaryDirectory() as directory,
            patch.object(self.api, "get_app_details_by_package_name", AsyncMock(return_value=details)),
            patch.object(self.api, "purchase", AsyncMock(return_value=DeliveryResponse(status=1))),
            self.assertRaises(EmptyDownloadsError),
        ):
            await self.api.download_app("example.app", Path(directory))
        self.assertEqual(self.requests, [])

    async def test_split_only_download_can_create_the_default_xapk_without_a_base(self) -> None:
        details = DetailsResponse()
        details.item.details.app_details.package_name = "example.app"
        details.item.details.app_details.version_code = 42
        details.item.offer.add(offer_type=1)
        delivery = DeliveryResponse(status=1)
        for name in ("config.en", "config.arm64_v8a"):
            delivery.app_delivery_data.split_delivery_data.add(
                name=name,
                download_url=f"https://example.invalid/{name}.apk",
                download_size=3,
            )
        self.body = b"apk"
        with (
            TemporaryDirectory() as directory,
            patch.object(self.api, "get_app_details_by_package_name", AsyncMock(return_value=details)),
            patch.object(self.api, "purchase", AsyncMock(return_value=delivery)),
        ):
            await self.api.download_app("example.app", Path(directory))
            with ZipFile(Path(directory) / "example.app.xapk") as archive:
                self.assertNotIn("base.apk", archive.namelist())
                self.assertNotIn("icon.png", archive.namelist())
                manifest = json.loads(archive.read("manifest.json"))
                self.assertNotIn("icon", manifest)
                self.assertEqual(
                    [entry["file"] for entry in manifest["split_apks"]],
                    ["config.en.apk", "config.arm64_v8a.apk"],
                )


class DeliveryParsingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.api = GooglePlayAPI.__new__(GooglePlayAPI)

    def test_empty_delivery_does_not_create_phantom_dex_metadata(self) -> None:
        self.assertEqual(self.api.parse_delivery_response("example.app", DeliveryResponse()), [])

    def test_expansion_file_type_and_kept_version_code_are_preserved(self) -> None:
        response = DeliveryResponse()
        response.app_delivery_data.additional_file.add(
            file_type=0,
            version_code=12,
            download_url="https://example.invalid/main",
            download_size=10,
        )
        response.app_delivery_data.additional_file.add(
            file_type=1,
            version_code=0,
            download_url="https://example.invalid/patch",
            download_size=2,
        )
        files = self.api.parse_delivery_response("example.app", response, version_code=42)
        self.assertEqual([file.name for file in files], ["main.12.example.app.obb", "patch.42.example.app.obb"])
        self.assertEqual([file.type for file in files], [PlayFileType.OBB, PlayFileType.PATCH])

    def test_a_split_only_delivery_needs_no_base_or_dex_url(self) -> None:
        response = DeliveryResponse()
        response.app_delivery_data.split_delivery_data.add(
            name="config.en",
            download_url="https://example.invalid/config",
            download_size=5,
        )
        files = self.api.parse_delivery_response("example.app", response)
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].name, "config.en.apk")

    def test_present_dex_without_a_url_is_not_downloaded(self) -> None:
        response = DeliveryResponse()
        response.app_delivery_data.dex_metadata.SetInParent()
        self.assertEqual(self.api.parse_delivery_response("example.app", response), [])

    def test_blank_artifact_urls_and_dex_only_responses_are_not_downloadable(self) -> None:
        response = DeliveryResponse()
        response.app_delivery_data.additional_file.add(file_type=0, download_url=" ")
        response.app_delivery_data.split_delivery_data.add(name="missing", download_url="")
        response.app_delivery_data.dex_metadata.download_url = "https://example.invalid/base.dm"
        self.assertEqual(self.api.parse_delivery_response("example.app", response), [])

    def test_split_dex_metadata_uses_a_distinct_dm_name(self) -> None:
        response = DeliveryResponse()
        split = response.app_delivery_data.split_delivery_data.add(
            name="config.en",
            download_url="https://example.invalid/config.apk",
            download_size=5,
        )
        split.dex_metadata.download_url = "https://example.invalid/config.dm"
        split.dex_metadata.download_size = 3
        files = self.api.parse_delivery_response("example.app", response)
        self.assertEqual([file.name for file in files], ["config.en.apk", "config.en.dm"])
        self.assertEqual(files[1].type, PlayFileType.DEX)
        self.assertEqual(files[1].size, 3)

    def test_patch_format_names_keep_the_previous_aliases(self) -> None:
        self.assertEqual([format_.value for format_ in PatchFormat], list(range(1, 14)))
        self.assertIs(PatchFormat.UNKNOWN_4, PatchFormat.GZIPPED_FILEBYFILE)
        self.assertIs(PatchFormat.UNKNOWN_5, PatchFormat.BROTLI_FILEBYFILE)
