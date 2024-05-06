from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
import os


class WaitElement:
    @staticmethod
    def wait_until_element_be_visible(browser, locator):
        return Wait(browser, float(os.environ["Timeout_Seconds"]), poll_frequency=1).until(
            EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_until_elements_are_visible(browser, locator):
        return Wait(browser, float(os.environ["Timeout_Seconds"]), poll_frequency=1).until(
            EC.visibility_of_all_elements_located(locator))

    @staticmethod
    def wait_alert_is_present(browser):
        return Wait(browser, float(os.environ["Timeout_Seconds"]), poll_frequency=1).until(
            EC.alert_is_present())
