# SPDX-FileCopyrightText: 2020-2025 Aurora OSS
# SPDX-FileCopyrightText: 2023 The Calyx Institute
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import time
from configparser import ConfigParser
from typing import TYPE_CHECKING

from pyplay.constants import DEVICES_PATH
from pyplay.exceptions import DeviceNotFoundError
from pyplay.playprotos.google_play import (
    AndroidBuildProto,
    AndroidCheckinProto,
    AndroidCheckinRequest,
    DeviceConfigurationProto,
    DeviceFeature,
)

if TYPE_CHECKING:
    from babel import Locale


def list_devices() -> list[str]:
    return [p.stem for p in DEVICES_PATH.iterdir()]


class Device:
    def __init__(self, codename: str, locale: Locale) -> None:
        self.codename = codename
        self.locale = locale

        devices = DEVICES_PATH.iterdir()
        device_props = next((props for props in devices if props.stem == codename), None)
        if not device_props:
            raise DeviceNotFoundError(device_name=codename, devices=[p.stem for p in devices])
        parser = ConfigParser()
        parser.read(device_props)
        self.properties = parser[codename]
        self.check_compatibility()

    def __repr__(self) -> str:
        return f"<Device {self.codename} ({self.properties.get('Build.MODEL', 'Unknown Model')})>"

    def override_properties(self, overrides: dict[str, str | None]) -> None:
        for key, value in overrides.items():
            if value is None:
                if key in self.properties:
                    del self.properties[key]
            else:
                self.properties[key] = str(value)

    @property
    def sdk_version(self) -> int:
        return self.properties.getint("Build.VERSION.SDK_INT", 0)

    @property
    def play_services_version(self) -> int:
        return self.properties.getint("GSF.version", 0)

    @property
    def mcc_mnc(self) -> str:
        return self.properties.get("SimOperator", "")

    @property
    def auth_user_agent_string(self) -> str:
        device = self.properties.get("Build.DEVICE", "")
        build_id = self.properties.get("Build.ID", "")
        return f"GoogleAuth/1.4 ({device} {build_id})"

    def _get_list_from_property(self, property_name: str) -> list[str]:
        return [item.strip() for item in self.properties.get(property_name, "").split(",") if item.strip()]

    @property
    def user_agent_string(self) -> str:
        params = [
            f"api={3}",
            f"versionCode={self.properties.get('Vending.version', '')}",
            f"sdk={self.properties.get('Build.VERSION.SDK_INT', '')}",
            f"device={self.properties.get('Build.DEVICE', '')}",
            f"hardware={self.properties.get('Build.HARDWARE', '')}",
            f"product={self.properties.get('Build.PRODUCT', '')}",
            f"platformVersionRelease={self.properties.get('Build.VERSION.RELEASE', '')}",
            f"model={self.properties.get('Build.MODEL', '')}",
            f"buildId={self.properties.get('Build.ID', '')}",
            f"isWideScreen={0}",
            f"supportedAbis={';'.join(self._get_list_from_property('Platforms'))}",
        ]
        version_str = self.properties.get("Vending.versionString")
        return f"Android-Finsky/{version_str} ({','.join(params)})"

    @property
    def device_configuration(self) -> DeviceConfigurationProto:
        return DeviceConfigurationProto(
            touch_screen=self.properties.getint("TouchScreen", 0),
            keyboard=self.properties.getint("Keyboard", 0),
            navigation=self.properties.getint("Navigation", 0),
            screen_layout=self.properties.getint("ScreenLayout", 0),
            has_hard_keyboard=self.properties.getboolean("HasHardKeyboard", False),
            has_five_way_navigation=self.properties.getboolean("HasFiveWayNavigation", False),
            low_ram_device=self.properties.getint("LowRamDevice", 0),
            max_num_of_cpu_cores=self.properties.getint("MaxNumOfCPUCores", 8),
            total_memory_bytes=self.properties.getint("TotalMemoryBytes", 8_589_935_000),
            device_class=0,
            screen_density=self.properties.getint("Screen.Density", 0),
            screen_width=self.properties.getint("Screen.Width", 0),
            screen_height=self.properties.getint("Screen.Height", 0),
            native_platform=self._get_list_from_property("Platforms"),
            system_shared_library=self._get_list_from_property("SharedLibraries"),
            system_available_feature=self._get_list_from_property("Features"),
            system_supported_locale=self._get_list_from_property("Locales"),
            gl_es_version=self.properties.getint("GL.Version", 0),
            gl_extension=self._get_list_from_property("GL.Extensions"),
            device_feature=[DeviceFeature(name=name, value=0) for name in self._get_list_from_property("Features")],
        )

    def generate_android_checkin_request(self) -> AndroidCheckinRequest:
        build = AndroidBuildProto(
            id=self.properties.get("Build.FINGERPRINT", ""),
            product=self.properties.get("Build.HARDWARE", ""),
            carrier=self.properties.get("Build.BRAND", ""),
            radio=self.properties.get("Build.RADIO", ""),
            bootloader=self.properties.get("Build.BOOTLOADER", ""),
            device=self.properties.get("Build.DEVICE", ""),
            sdk_version=self.properties.getint("Build.VERSION.SDK_INT", 0),
            model=self.properties.get("Build.MODEL", ""),
            manufacturer=self.properties.get("Build.MANUFACTURER", ""),
            build_product=self.properties.get("Build.PRODUCT", ""),
            client=self.properties.get("Client", ""),
            ota_installed=self.properties.getboolean("OtaInstalled", False),
            timestamp=int(time.time()),
            google_services=self.properties.getint("GSF.version", 0),
        )
        checkin = AndroidCheckinProto(
            build=build,
            last_checkin_msec=0,
            cell_operator=self.properties.get("CellOperator", ""),
            sim_operator=self.properties.get("SimOperator", ""),
            roaming=self.properties.get("Roaming", ""),
            user_number=0,
        )

        return AndroidCheckinRequest(
            id=0,
            checkin=checkin,
            locale=str(self.locale),
            time_zone=self.properties.get("TimeZone", ""),
            version=3,
            device_configuration=self.device_configuration,
            fragment=0,
        )

    def check_compatibility(self) -> None:
        required_fields = [
            "Build.HARDWARE",
            "Build.RADIO",
            "Build.BOOTLOADER",
            "Build.FINGERPRINT",
            "Build.BRAND",
            "Build.DEVICE",
            "Build.VERSION.SDK_INT",
            "Build.MODEL",
            "Build.MANUFACTURER",
            "Build.PRODUCT",
            "TouchScreen",
            "Keyboard",
            "Navigation",
            "ScreenLayout",
            "HasHardKeyboard",
            "HasFiveWayNavigation",
            "GL.Version",
            "GSF.version",
            "Vending.version",
            "Screen.Density",
            "Screen.Width",
            "Screen.Height",
            "Platforms",
            "SharedLibraries",
            "Features",
            "Locales",
            "CellOperator",
            "SimOperator",
            "Roaming",
            "Client",
            "TimeZone",
            "GL.Extensions",
        ]
        if missing := [field for field in required_fields if field not in self.properties]:
            msg = f"Device '{self.codename}' is missing required fields: {missing}"
            raise ValueError(msg)

        if "Vending.versionString" not in self.properties:
            version = self.properties["Vending.version"]
            if len(version) > 6:  # noqa: PLR2004
                version_string = list(version[2:6])
                version_string.insert(2, ".")
                version_string.insert(1, ".")
                self.properties["Vending.versionString"] = "".join(version_string)
            else:
                self.properties["Vending.versionString"] = "7.1.15"

        if "Build.ID" not in self.properties or "Build.VERSION.RELEASE" not in self.properties:
            parts = self.properties.get("Build.FINGERPRINT", "").split("/")
            release = build_id = ""
            if len(parts) > 5:  # noqa: PLR2004
                i = next((idx for idx, comp in enumerate(parts) if ":" in comp), -1)
                if i != -1:
                    release = parts[i].split(":", 1)[1]
                    if i + 1 < len(parts):
                        build_id = parts[i + 1]
            self.properties.setdefault("Build.ID", build_id)
            self.properties.setdefault("Build.VERSION.RELEASE", release)
