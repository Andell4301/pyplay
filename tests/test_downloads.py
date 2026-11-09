# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import unittest
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import AsyncMock, patch
from zipfile import ZipFile

import httpx

from pyplay import AuthData, GooglePlayAPI, PlayFile
from pyplay.constants import PlayFileType
from pyplay.playprotos.google_play import DetailsResponse, ResponseWrapperApi


def app_details() -> DetailsResponse:
    details = DetailsResponse()
    details.item.title = "Example"
    details.item.details.app_details.package_name = "example.app"
    details.item.details.app_details.version_code = 1
    details.item.offer.add(offer_type=1)
    return details


def play_file(name: str = "base.apk", *, size: int = 3, file_type: PlayFileType = PlayFileType.BASE) -> PlayFile:
    return PlayFile(name, f"https://example.invalid/{name}?token=download-secret", size, file_type)


class DownloadTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.api = GooglePlayAPI(AuthData(gsf_id="test-gsf", auth_token="test-auth"), locale="en_US")
        await self.api.client.aclose()
        self.status = 200
        self.content = b"apk"
        self.requests: list[httpx.Request] = []

        def respond(request: httpx.Request) -> httpx.Response:
            self.requests.append(request)
            return httpx.Response(self.status, content=self.content)

        self.api.client = httpx.AsyncClient(transport=httpx.MockTransport(respond))
        self.addAsyncCleanup(self.api.client.aclose)
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.output_dir = Path(self.directory.name)

    async def download(self, files: list[PlayFile], *, include_dex: bool = False) -> None:
        with (
            patch.object(self.api, "get_app_details_by_package_name", AsyncMock(return_value=app_details())),
            patch.object(self.api, "purchase", AsyncMock(return_value=None)),
            patch.object(self.api, "parse_delivery_response", return_value=files),
        ):
            await self.api.download_app("example.app", self.output_dir, use_xapk=False, include_dex=include_dex)

    async def test_valid_download_is_saved(self) -> None:
        await self.download([play_file()])
        self.assertEqual((self.output_dir / "base.apk").read_bytes(), b"apk")

    async def test_invalid_sizes_do_not_overwrite_existing_files(self) -> None:
        output_path = self.output_dir / "base.apk"
        output_path.write_bytes(b"existing download")
        for expected_size in (-1, 2, 4):
            with self.subTest(expected_size=expected_size):
                with self.assertRaises((ValueError, OSError)):
                    await self.download([play_file(size=expected_size)])
                self.assertEqual(output_path.read_bytes(), b"existing download")

    async def test_http_error_does_not_create_a_file_or_expose_download_token(self) -> None:
        self.status = 403
        with self.assertRaises(httpx.HTTPStatusError) as caught:
            await self.download([play_file()])
        self.assertEqual(caught.exception.response.status_code, 403)
        self.assertNotIn("download-secret", str(caught.exception))
        self.assertFalse((self.output_dir / "base.apk").exists())

    async def test_excluded_dex_is_not_requested_or_overwritten(self) -> None:
        dex_path = self.output_dir / "base.dm"
        dex_path.write_bytes(b"keep this dex")
        await self.download([play_file(), play_file("base.dm", file_type=PlayFileType.DEX)])
        self.assertEqual([request.url.path for request in self.requests], ["/base.apk"])
        self.assertEqual(dex_path.read_bytes(), b"keep this dex")

    async def test_each_downloaded_file_has_its_size_checked(self) -> None:
        files = [play_file(), play_file("config.apk", size=4, file_type=PlayFileType.SPLIT)]
        with self.assertRaises((ValueError, OSError)):
            await self.download(files)
        self.assertEqual((self.output_dir / "base.apk").read_bytes(), b"apk")
        self.assertFalse((self.output_dir / "config.apk").exists())

    async def test_download_logs_include_totals_without_signed_urls(self) -> None:
        with self.assertLogs("pyplay.api", level="DEBUG") as captured:
            await self.download([play_file()])
        rendered = "\n".join(captured.output)
        self.assertNotIn("download-secret", rendered)
        totals = [record for record in captured.records if hasattr(record, "downloaded_bytes")]
        self.assertTrue(totals, "download completion should include downloaded byte totals")
        self.assertEqual(totals[-1].downloaded_bytes, 3)

    async def test_package_name_newlines_are_escaped_in_download_logs(self) -> None:
        invalid_output_dir = self.output_dir / "existing-file"
        invalid_output_dir.write_bytes(b"existing content")

        with self.assertLogs("pyplay.api", level="INFO") as captured, self.assertRaises(ValueError):
            await self.api.download_app("example\nINJECT", invalid_output_dir)

        for record in captured.records:
            self.assertNotIn("\n", record.getMessage())
        self.assertTrue(any(r"example\nINJECT" in record.getMessage() for record in captured.records))


class ProfileTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.api = GooglePlayAPI(AuthData(gsf_id="test-gsf", auth_token="test-auth"), locale="en_US")
        await self.api.client.aclose()
        self.status = 200
        self.body = b""
        self.api.client = httpx.AsyncClient(
            transport=httpx.MockTransport(lambda _: httpx.Response(self.status, content=self.body))
        )
        self.addAsyncCleanup(self.api.client.aclose)

    async def test_profile_404_returns_none(self) -> None:
        self.status = 404
        self.assertIsNone(await self.api.get_user_profile())

    async def test_other_profile_failures_propagate(self) -> None:
        for status in (401, 403, 429, 500):
            self.status = status
            with self.subTest(status=status):
                with self.assertRaises(httpx.HTTPStatusError) as caught:
                    await self.api.get_user_profile()
                self.assertEqual(caught.exception.response.status_code, status)

    async def test_successful_profile_is_decoded(self) -> None:
        wrapper = ResponseWrapperApi()
        wrapper.payload.user_profile_response.user_profile.name = "Example User"
        self.body = wrapper.SerializeToString()
        profile = await self.api.get_user_profile()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.name, "Example User")


class XapkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.api = GooglePlayAPI.__new__(GooglePlayAPI)
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.output_dir = Path(self.directory.name)
        apk_data = BytesIO()
        with ZipFile(apk_data, "w") as apk:
            apk.writestr("AndroidManifest.xml", b"manifest")
        (self.output_dir / "base.apk").write_bytes(apk_data.getvalue())
        (self.output_dir / "config.apk").write_bytes(b"config")
        self.files = [play_file(), play_file("config.apk", file_type=PlayFileType.SPLIT)]

    def test_excluded_dex_survives_cleanup(self) -> None:
        dex_path = self.output_dir / "base.dm"
        dex_path.write_bytes(b"existing dex")
        files = [*self.files, play_file("base.dm", file_type=PlayFileType.DEX)]
        self.api.make_xapk("example.app", app_details(), files, self.output_dir, include_dex=False)
        self.assertEqual(dex_path.read_bytes(), b"existing dex")
        self.assertFalse((self.output_dir / "base.apk").exists())
        self.assertFalse((self.output_dir / "config.apk").exists())
        with ZipFile(self.output_dir / "example.app.xapk") as archive:
            self.assertIn("base.apk", archive.namelist())
            self.assertNotIn("base.dm", archive.namelist())

    def test_archive_creation_failure_preserves_inputs(self) -> None:
        message = "cannot read icon"
        with (
            patch.object(self.api, "extract_icon_from_apk", side_effect=OSError(message)),
            self.assertRaises(OSError),
        ):
            self.api.make_xapk("example.app", app_details(), self.files, self.output_dir)
        self.assertTrue((self.output_dir / "base.apk").exists())
        self.assertTrue((self.output_dir / "config.apk").exists())
        self.assertTrue((self.output_dir / "manifest.json").exists())

    def test_cleanup_failure_warns_and_continues_after_archive_is_created(self) -> None:
        original_unlink = Path.unlink

        def unlink(path: Path, *, missing_ok: bool = False) -> None:
            if path.name == "base.apk":
                message = "cannot delete input"
                raise PermissionError(message)
            original_unlink(path, missing_ok=missing_ok)

        with patch.object(Path, "unlink", new=unlink), self.assertLogs("pyplay.api", level="WARNING") as captured:
            self.api.make_xapk("example.app", app_details(), self.files, self.output_dir)
        self.assertEqual(captured.records[-1].cleanup_failures, 1)
        self.assertTrue((self.output_dir / "base.apk").exists())
        self.assertFalse((self.output_dir / "config.apk").exists())
        self.assertFalse((self.output_dir / "manifest.json").exists())
        with ZipFile(self.output_dir / "example.app.xapk") as archive:
            self.assertIsNone(archive.testzip())
