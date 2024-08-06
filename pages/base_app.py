from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def find_ellement_with_text(self, locator, text, time=20):
        """
        Функция поиска элемента с указанным текстом на странице.
        """
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Элемент {locator} не найден"
            )

    def find_element(self, locator, time=20):
        """
        Функция поиска элемента на странице.
        """
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
            )
        self.scroll_to_element(element)
        return element

    def find_elements(self, locator, time=20):
        """
        Функция поиска элементов на странице.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы {locator} не найдены"
            )

    def go_to_site(self):
        """
        Функция для перехода по ссылке.
        """
        return self.driver.get(self.base_url)

    def switch_tab(self, number):
        """
        Функция для смены вкладке в режиме тестирования.
        """
        self.driver.switch_to.window(self.driver.window_handles[number])
        self.driver.refresh()

    def scroll_to_element(self, element):
        """
        Функция для прокрутки страницы до указонного элемента.
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)
