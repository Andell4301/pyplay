# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from babel import Locale

from pyplay.api import AuthData, GooglePlayAPI, PlayFile
from pyplay.device import Device, list_devices
from pyplay.exceptions import (
    AppNotFoundError,
    AppNotPurchasedError,
    AppNotSupportedError,
    AppRemovedError,
    AuthExceptionError,
    DeviceNotFoundError,
    EmptyDownloadsError,
    PurchaseError,
    ServerError,
    UnknownError,
)

try:
    __version__ = version("pyplay")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__all__ = [
    "AppNotFoundError",
    "AppNotPurchasedError",
    "AppNotSupportedError",
    "AppRemovedError",
    "AuthData",
    "AuthExceptionError",
    "Device",
    "DeviceNotFoundError",
    "EmptyDownloadsError",
    "GooglePlayAPI",
    "Locale",
    "PlayFile",
    "PurchaseError",
    "ServerError",
    "UnknownError",
    "__version__",
    "list_devices",
]
