# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import unittest

from babel import Locale

from pyplay.device import Device, list_devices


class DeviceTests(unittest.TestCase):
    def test_googlebook_profiles_load_with_unescaped_fingerprints(self) -> None:
        profiles = {
            "acer_googlebook_14_moonstone": "moonstone",
            "asus_googlebook_14_lapis": "lapis",
            "dell_xps_googlebook_mica": "mica",
            "hp_googlebook_14_quartz": "quartz",
            "lenovo_googlebook_15_ruby": "ruby",
        }
        available = list_devices()

        for profile, expected_device in profiles.items():
            with self.subTest(profile=profile):
                self.assertIn(profile, available)
                device = Device(profile, Locale.parse("en_US"))
                build = device.generate_android_checkin_request().checkin.build
                self.assertEqual(build.device, expected_device)
                self.assertIn(":17/", build.id)
                self.assertNotIn("\\", build.id)
                self.assertIn("android.hardware.type.pc", device.device_configuration.system_available_feature)

    def test_user_languages_omit_script_and_keep_country(self) -> None:
        device = Device("google_pixel_9a", Locale.parse("zh_Hans_CN"))

        self.assertEqual(device.user_languages, "zh_CN")
        self.assertEqual(str(device.locale).replace("_", "-"), "zh-Hans-CN")

    def test_user_languages_keep_regular_locale(self) -> None:
        device = Device("google_pixel_9a", Locale.parse("en_US"))

        self.assertEqual(device.user_languages, "en_US")

    def test_user_languages_accept_locale_without_country(self) -> None:
        device = Device("google_pixel_9a", Locale.parse("en"))

        self.assertEqual(device.user_languages, "en")
