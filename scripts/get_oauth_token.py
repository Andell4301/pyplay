# ruff: noqa: T201

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_oauth_token() -> str:
    options = webdriver.ChromeOptions()
    options.add_argument(
        argument="--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"  # noqa: E501
    )
    options.add_argument(argument="--disable-blink-features=AutomationControlled")
    options.add_experimental_option(name="excludeSwitches", value=["enable-automation"])
    options.add_experimental_option(name="useAutomationExtension", value=False)
    with webdriver.Chrome(options=options) as driver:
        # Some other scripts use https://accounts.google.com/EmbeddedSetup
        # That will work here too, but for me, using OAuth from that page to
        # gen an AAS token gives a 4xx error, whereas this one works
        driver.get("https://accounts.google.com/embedded/setup/v2/android")
        WebDriverWait(driver, 300).until(lambda d: d.get_cookie("oauth_token"))
        return driver.get_cookie("oauth_token")["value"]  # type: ignore[reportOptionalSubscript]


if __name__ == "__main__":
    try:
        token = get_oauth_token()
        print(f"OAuth Token: {token}")
    except Exception as e:
        print(f"Error retrieving OAuth token: {e}")
