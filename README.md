# Google Play API Python Library

A Python library for interacting with the Google Play API.

This would not be possible without the excellent work of [AuroraOSS's GPlayApi](https://gitlab.com/AuroraOSS/gplayapi) and [EFF's rs-google-play](https://github.com/EFForg/rs-google-play), both of which this project draws from and was inspired by.

The protobuf files and device configs are sourced from both projects. The protobuf definitions have been modified for snake_case naming and a few consistency changes with the Rust version of this library.

This is an unofficial client for interacting with Google Play APIs. It is not affiliated with, endorsed by, or supported by Google. Users are responsible for complying with Google Play’s terms and any applicable laws or third-party licenses.


## Notes

- I try to keep this reasonably up to date with relevant changes from Aurora and EFF.
- This library will generally follow updates I make in the Rust version.
- This code is primarily for my own use, so I cannot guarantee that breaking changes will not happen.
- I did not originally plan to open-source this, so the git history was wiped when publishing. This project has been around for a while, though.
- Not all code paths have been tested, especially areas I do not personally use.

## Usage

```py
async def main():
    auth_data = AuthData(your_creds)
    async with GooglePlayAPI(auth_data=auth_data, device="codename", locale="locale") as api:
        await api.setup()
        await api.download_app("package_name", output_dir=Path("."))
```