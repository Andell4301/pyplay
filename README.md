# Google Play API Python Library

A Python library for interacting with the Google Play API.

This would not be possible without the excellent work of [AuroraOSS's GPlayApi](https://gitlab.com/AuroraOSS/gplayapi) and [EFF's rs-google-play](https://github.com/EFForg/rs-google-play), both of which this project draws from and was inspired by.

The protobuf files and device configs are sourced from both projects. The protobuf definitions have been modified for snake_case naming and a few consistency changes with the Rust version of this library.

This is an unofficial client for interacting with Google Play APIs. It is not affiliated with, endorsed by, or supported by Google. Users are responsible for complying with Google Play’s terms and any applicable laws or third-party licenses.


## Notes

- I try to keep this reasonably up to date with relevant changes from Aurora and EFF.
- This library will generally follow updates I make in the [Rust version](https://github.com/Andell4301/playrs) I update in tandem.
- This code is primarily for my own use, so I cannot guarantee that breaking changes will not happen.
- I did not originally plan to open source this, so the git history was wiped when publishing. This project has been around for a while, though.
- Not all code paths have been tested, especially areas I do not personally use.

## Usage

```py
async def main():
    auth_data = AuthData(your_creds)
    async with GooglePlayAPI(auth_data=auth_data, device="codename", locale="locale") as api:
        await api.setup()
        await api.download_app("package_name", output_dir=Path("."))
```

For streams that return items and a node tree, use `await api.get_stream_tree_response("getHomeStream?c=3")`. The returned `StreamResponse` has `item` and `tree` fields. The same method accepts child URLs and page URLs with a `ptkn` cursor.

Delivery methods accept `installed_derived_apk_id`, `installed_frosting_id`, and `patch_formats` alongside a positive `installed_version_code`. The single `patch_format` argument is also supported. Downloading or applying a binary patch is the caller's responsibility.

## Logging

Pyplay uses Python's standard `logging` module and leaves handlers and log levels to the calling application. To send its debug logs to stderr:

```py
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,
    stream=sys.stderr,
    format="%(levelname)s %(name)s: %(message)s",
)
logging.getLogger("pyplay").setLevel(logging.DEBUG)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
```

Set the `pyplay` logger to `logging.INFO` for authentication and download progress, or `logging.ERROR` to suppress informational and warning messages. Request logs include method and route context; structured log records also provide request IDs, timing, status, and response sizes for custom handlers. Download completion records include byte and file counts.

Pyplay's own logs and request error messages omit URL query strings and complete credential values. `repr(AuthData(...))` hides emails, IDs, and cookies. Token fields show only a three-character prefix and suffix when the value contains at least twelve printable ASCII characters without whitespace; shorter or non-printable tokens remain redacted. `repr(PlayFile(...))` hides its download URL.

These safeguards apply to Pyplay's own representations, logs, and error messages. HTTPX and other dependencies have their own logging behavior. Keep their log levels at `WARNING` or higher as shown above: HTTPX request logs can include signed download URLs and other sensitive query parameters. Accessing credential fields directly, logging raw request headers, or printing the OAuth helper's output still exposes complete credentials.

## Tests

With the project dependencies installed, run the regression tests without making network requests:

```sh
python -m unittest discover -s tests -v
```
