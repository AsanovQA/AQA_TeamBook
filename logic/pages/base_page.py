from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(ec.visibility_of_all_elements_located(locator))

    # для будущих тестов
    # def element_is_present(self, locator, timeout=5):
    #     return Wait(self.browser, timeout).until(ec.presence_of_element_located(locator))
    #
    # def elements_are_present(self, locator, timeout=5):
    #     return Wait(self.browser, timeout).until(ec.presence_of_all_elements_located(locator))
    #
    # def element_is_not_visible(self, locator, timeout=5):
    #     return Wait(self.browser, timeout).until(ec.invisibility_of_element_located(locator))
    #
    # def element_is_clickable(self, locator, timeout=5):
    #     return Wait(self.browser, timeout).until(ec.element_to_be_clickable(locator))
