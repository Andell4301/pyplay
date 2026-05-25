# SPDX-License-Identifier: GPL-3.0-or-later


class DeviceNotFoundError(Exception):
    def __init__(
        self, reason: str = "Device not found", device_name: str | None = None, devices: list[str] | None = None
    ) -> None:
        self.reason = reason
        self.device_name = device_name
        self.devices = devices
        message = self.reason
        if self.device_name:
            message += f": {self.device_name}"
        if self.devices:
            message += f"\nAvailable devices: {', '.join(self.devices)}"
        super().__init__(message)


class AuthExceptionError(Exception):
    def __init__(self, reason: str = "Authentication Error") -> None:
        self.reason = reason
        super().__init__(self.reason)


class AppNotPurchasedError(Exception):
    def __init__(self, reason: str = "App not purchased") -> None:
        self.reason = reason
        super().__init__(self.reason)


class AppNotFoundError(Exception):
    def __init__(self, app_name: str) -> None:
        self.reason = f"App '{app_name}' was not found. Maybe it's not available in your country or on your device?"
        super().__init__(self.reason)


class AppRemovedError(Exception):
    def __init__(self, reason: str = "App removed from Play Store") -> None:
        self.reason = reason
        super().__init__(self.reason)


class AppNotSupportedError(Exception):
    def __init__(self, reason: str = "App not supported") -> None:
        self.reason = reason
        super().__init__(self.reason)


class EmptyDownloadsError(Exception):
    def __init__(self, reason: str = "File list empty") -> None:
        self.reason = reason
        super().__init__(self.reason)


class UnknownError(Exception):
    def __init__(self, reason: str = "Unknown error") -> None:
        self.reason = reason
        super().__init__(self.reason)


class ServerError(Exception):
    def __init__(self, code: int = 500, reason: str = "Server error") -> None:
        self.code = code
        self.reason = reason
        super().__init__(f"{self.code}: {self.reason}")


class PurchaseError(Exception):
    def __init__(self, reason: str = "Purchase error") -> None:
        self.reason = reason
        super().__init__(self.reason)
