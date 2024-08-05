from selenium.webdriver.chrome.options import Options


class ChromeOptions:
    driver_options = Options()
    driver_options.add_argument("--log-level=3")
    driver_options.add_experimental_option('excludeSwitches',
                                           ['enable-logging'])
