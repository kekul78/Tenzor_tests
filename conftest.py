import pytest
from selenium import webdriver

from chromedriver_options import ChromeOptions


@pytest.fixture(scope="session")
def browser():
    """
    Микстура для запуска ВебДрайвера
    """
    driver = webdriver.Chrome(options=ChromeOptions.driver_options)
    driver.maximize_window()
    yield driver

    driver.quit()
