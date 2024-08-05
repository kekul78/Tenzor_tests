from selenium.common.exceptions import NoSuchElementException

from pages.base_app import BasePage


class TestHelper(BasePage):

    def go_to_PATH(self, locator):
        search_filed = self.find_element(locator, time=2)
        try:
            search_filed.click()
        except:
            self.driver.execute_script("arguments[0].click();", search_filed)

    def check_exist_element(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def get_photo_size(self, locator):
        photo = self.find_elements(locator)
        data = [[temp.get_attribute('width'),
                 temp.get_attribute('height')] for temp in photo]
        return data
