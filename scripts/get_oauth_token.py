# ruff: noqa: T201
import undetected
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import WebDriverWait
from undetected.patcher import Patcher


def get_chrome_binary() -> str:
    return SeleniumManager().binary_paths(["--browser", "chrome", "--browser-version", "stable"])["browser_path"]


def get_oauth_token() -> str:
    chrome_binary = get_chrome_binary()
    Patcher.patch(browser_executable_path=chrome_binary)

    with undetected.Chrome(browser_executable_path=chrome_binary, user_multi_procs=True) as driver:
        # Some other scripts use https://accounts.google.com/EmbeddedSetup
        # That will work here too, but for me, using OAuth from that page to
        # gen an AAS token gives a 4xx error, whereas this one works
        driver.get("https://accounts.google.com/embedded/setup/v2/android")
        WebDriverWait(driver, 300).until(lambda d: d.get_cookie("oauth_token"))
        return driver.get_cookie("oauth_token")["value"]


if __name__ == "__main__":
    try:
        token = get_oauth_token()
        print(f"OAuth Token: {token}")
    except Exception as e:
        print(f"Error retrieving OAuth token: {e}")
