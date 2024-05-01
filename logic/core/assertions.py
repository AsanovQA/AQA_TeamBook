import os

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Assertion:
    @staticmethod
    def assert_is_invisible(browser, locator):
        try:
            WebDriverWait(browser, float(os.environ["Timeout_Seconds"]), poll_frequency=1).until(
                EC.invisibility_of_element_located(locator)
            )
            return False
        except TimeoutException:
            return True
