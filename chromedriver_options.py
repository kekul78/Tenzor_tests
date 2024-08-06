from selenium.webdriver.chrome.options import Options

from tests.config import DOWNLOAD_PATH


class ChromeOptions:
    driver_options = Options()
    driver_options.add_argument("--log-level=3")
    driver_options.add_experimental_option('excludeSwitches',
                                           ['enable-logging'])
    driver_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_PATH,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
