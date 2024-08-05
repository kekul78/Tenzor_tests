from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=20):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден {locator}"
            )
        self.scroll_to_element(element)
        return element

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы не найдены {locator}"
            )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_tab(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])
        self.driver.refresh()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)
