# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import traceback
import unittest
from typing import TYPE_CHECKING
from urllib.parse import parse_qs

import httpx
from google.protobuf.message import DecodeError

from pyplay.api import AuthData, GooglePlayAPI, PlayFile
from pyplay.constants import PlayFileType, TokenService
from pyplay.exceptions import AuthExceptionError

if TYPE_CHECKING:
    from collections.abc import Callable


class RepresentationTests(unittest.TestCase):
    def test_auth_data_hides_full_tokens_and_previews_only_the_edges(self) -> None:
        token = "abcdefghijklmnopqrstuvwxyz"
        credentials = AuthData(
            aas_token=token,
            auth_token=token,
            oauth_login_token=token,
            ac2dm_token=token,
            android_check_in_token=token,
            device_check_in_consistency_token=token,
            device_config_token=token,
            experiments_config_token=token,
            gcm_token=token,
        )

        rendered = repr(credentials)

        self.assertNotIn(token, rendered)
        self.assertIn("abc…xyz", rendered)
        for name in credentials.__dataclass_fields__:
            self.assertIn(name, rendered)

    def test_auth_data_redacts_short_non_ascii_and_control_character_tokens(self) -> None:
        for token in ("short", "abcdefghijk", "abc\ndefghijklmnop", "abc defghijklmnop", "åbcdefghijklmnop"):
            with self.subTest(token=token):
                rendered = repr(AuthData(auth_token=token))
                self.assertNotIn(token, rendered)
                self.assertNotIn(repr(token), rendered)
                self.assertIn("<redacted>", rendered)

    def test_auth_data_accepts_the_minimum_preview_length(self) -> None:
        rendered = repr(AuthData(auth_token="abcdefghijkl"))
        self.assertIn("abc…jkl", rendered)
        self.assertNotIn("abcdefghijkl", rendered)

    def test_auth_data_always_redacts_email_id_and_cookie(self) -> None:
        credentials = AuthData(
            email="private-email@example.invalid",
            gsf_id="private-gsf-id-value",
            dfe_cookie="private-cookie-value",
        )

        rendered = repr(credentials)

        self.assertNotIn(credentials.email, rendered)
        self.assertNotIn(credentials.gsf_id, rendered)
        self.assertNotIn(credentials.dfe_cookie, rendered)
        self.assertIn("<redacted>", rendered)

    def test_play_file_representation_hides_the_complete_url(self) -> None:
        file = PlayFile(
            name="base.apk",
            url="https://example.invalid/base.apk?token=private-download-token",
            size=20,
            type=PlayFileType.BASE,
        )

        rendered = repr(file)

        self.assertNotIn("example.invalid", rendered)
        self.assertNotIn("private-download-token", rendered)
        self.assertIn("base.apk", rendered)
        self.assertIn("<redacted>", rendered)


class HTTPLoggingTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.api = GooglePlayAPI(AuthData(gsf_id="test-gsf-id", auth_token="test-auth-token"), locale="en_US")
        await self.api.client.aclose()
        self.api.client = httpx.AsyncClient(
            transport=httpx.MockTransport(lambda _: httpx.Response(200, content=b"response"))
        )

    async def asyncTearDown(self) -> None:
        await self.api.client.aclose()

    async def replace_transport(self, handler: Callable[[httpx.Request], httpx.Response]) -> None:
        await self.api.client.aclose()
        self.api.client = httpx.AsyncClient(transport=httpx.MockTransport(handler))

    async def test_requests_log_safe_routes_and_response_metrics(self) -> None:
        url = "https://example.invalid/fdfe/details?token=private-query-token#private-fragment"

        with self.assertLogs("pyplay.api", level="DEBUG") as captured:
            response = await self.api._request("GET", url)

        self.assertEqual(response.content, b"response")
        diagnostics = "\n".join(repr(record.__dict__) for record in captured.records)
        self.assertNotIn("private-query-token", diagnostics)
        self.assertNotIn("private-fragment", diagnostics)
        self.assertIn("/fdfe/details", diagnostics)
        self.assertIn("GET", diagnostics)
        records = [record for record in captured.records if hasattr(record, "response_bytes")]
        self.assertTrue(records, "response logs should include the received byte count")
        record = records[-1]
        self.assertEqual(record.response_bytes, len(response.content))
        self.assertGreaterEqual(record.elapsed_ms, 0)
        self.assertIsInstance(record.request_id, int)

    async def test_request_ids_distinguish_requests(self) -> None:
        with self.assertLogs("pyplay.api", level="DEBUG") as captured:
            await self.api._request("GET", "https://example.invalid/first")
            await self.api._request("GET", "https://example.invalid/second")

        response_logs = [record for record in captured.records if hasattr(record, "response_bytes")]
        self.assertEqual(len(response_logs), 2)
        self.assertNotEqual(response_logs[0].request_id, response_logs[1].request_id)

    async def test_control_characters_in_routes_are_escaped_in_logs(self) -> None:
        url = "https://example.invalid/fdfe/line%0Abreak?token=private-newline-token"

        with self.assertLogs("pyplay.api", level="DEBUG") as captured:
            await self.api._request("GET", url)

        for record in captured.records:
            rendered = record.getMessage()
            self.assertNotIn("\n", rendered)
            self.assertNotIn("private-newline-token", rendered)
        self.assertTrue(any(r"\n" in record.getMessage() for record in captured.records))

    async def test_invalid_url_errors_do_not_echo_raw_input(self) -> None:
        url = "https://example.invalid:private-invalid-port/fdfe/details?token=private-invalid-token"

        with self.assertLogs("pyplay.api", level="DEBUG") as captured:
            try:
                await self.api._request("GET", url)
            except httpx.InvalidURL as error:
                rendered = "".join(traceback.format_exception(error))
                self.assertNotIn("private-invalid-port", rendered)
                self.assertNotIn("private-invalid-token", rendered)
                self.assertIn("GET", str(error))
            else:
                self.fail("an invalid URL must still raise InvalidURL")
        self.assertNotIn("private-invalid-port", "\n".join(captured.output))
        self.assertNotIn("private-invalid-token", "\n".join(captured.output))

    async def test_http_status_errors_preserve_status_and_hide_query_in_tracebacks(self) -> None:
        await self.replace_transport(lambda _: httpx.Response(403))
        url = "https://example.invalid/fdfe/delivery?dtok=private-delivery-token"

        try:
            await self.api._request("GET", url)
        except httpx.HTTPStatusError as error:
            self.assertEqual(error.response.status_code, 403)
            rendered = "".join(traceback.format_exception(error))
            self.assertNotIn("private-delivery-token", str(error))
            self.assertNotIn("private-delivery-token", repr(error))
            self.assertNotIn("private-delivery-token", rendered)
            self.assertIn("GET", str(error))
            self.assertIn("/fdfe/delivery", str(error))
        else:
            self.fail("unsuccessful responses must still raise HTTPStatusError")

    async def test_transport_errors_have_safe_request_context(self) -> None:
        def fail(request: httpx.Request) -> httpx.Response:
            message = f"Could not connect to {request.url}"
            raise httpx.ConnectError(message, request=request)

        await self.replace_transport(fail)
        url = "https://example.invalid/fdfe/delivery?dtok=private-transport-token"

        try:
            await self.api._request("GET", url)
        except httpx.RequestError as error:
            self.assertIs(type(error), httpx.ConnectError)
            rendered = "".join(traceback.format_exception(error))
            self.assertNotIn("private-transport-token", str(error))
            self.assertNotIn("private-transport-token", rendered)
            self.assertIn("GET", str(error))
            self.assertIn("/fdfe/delivery", str(error))
        else:
            self.fail("transport failures must still raise a request error")

    async def test_invalid_protobuf_includes_safe_request_context(self) -> None:
        await self.replace_transport(lambda _: httpx.Response(200, content=b"\xff"))
        url = "https://example.invalid/fdfe/details?token=private-decode-token"

        with self.assertRaises(DecodeError) as raised:
            await self.api._play_request("GET", url)

        self.assertNotIn("private-decode-token", str(raised.exception))
        self.assertIn("GET", str(raised.exception))
        self.assertIn("/fdfe/details", str(raised.exception))

    async def test_auth_credentials_use_query_parameters_against_an_empty_body(self) -> None:
        requests: list[httpx.Request] = []

        def respond(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, content=b"Token=generated-aas-token\nAuth=generated-auth-token")

        self.api.auth_data.email = "private-email@example.invalid"
        self.api.auth_data.oauth_login_token = "private-oauth-token"
        self.api.auth_data.aas_token = "private-aas-token"
        await self.replace_transport(respond)

        await self.api.generate_aas_token()
        await self.api.generate_token(TokenService.GOOGLEPLAY)

        self.assertEqual(len(requests), 2)
        for request, expected_token in zip(requests, ("private-oauth-token", "private-aas-token"), strict=True):
            with self.subTest(token=expected_token):
                self.assertEqual(request.method, "POST")
                self.assertEqual(request.content, b"")
                query = parse_qs(request.url.query.decode())
                self.assertEqual(query["Token"], [expected_token])
                self.assertEqual(query["Email"], [self.api.auth_data.email])

    async def test_aas_token_failures_do_not_dump_auth_response(self) -> None:
        self.api.auth_data.email = "test@example.invalid"
        self.api.auth_data.oauth_login_token = "private-oauth-token"
        await self.replace_transport(
            lambda _: httpx.Response(200, content=b"Error=BadAuthentication\nSecret=private-response-value")
        )

        with self.assertRaises((ValueError, AuthExceptionError)) as raised:
            await self.api.generate_aas_token()

        self.assertNotIn("private-response-value", str(raised.exception))
        self.assertNotIn("private-oauth-token", str(raised.exception))

    async def test_service_token_failures_do_not_dump_auth_response(self) -> None:
        self.api.auth_data.email = "test@example.invalid"
        self.api.auth_data.aas_token = "private-aas-token"
        await self.replace_transport(
            lambda _: httpx.Response(200, content=b"Error=BadAuthentication\nSecret=private-response-value")
        )

        with self.assertRaises(AuthExceptionError) as raised:
            await self.api.generate_token(TokenService.GOOGLEPLAY)

        self.assertNotIn("private-response-value", str(raised.exception))
        self.assertNotIn("private-aas-token", str(raised.exception))

    async def test_auth_setup_logs_when_credentials_are_reused(self) -> None:
        with self.assertLogs("pyplay.api", level="INFO") as captured:
            await self.api.setup()

        records = [record for record in captured.records if getattr(record, "reused", False)]
        self.assertTrue(records, "setup should identify reused credentials")
        self.assertNotIn("test-auth-token", "\n".join(captured.output))
