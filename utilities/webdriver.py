from selenium import webdriver
from utilities.enums import Driver
from utilities.functions import get_platform
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverClass:
    def __init__(self, driver: webdriver):
        if get_platform() == 'darwin':
            if driver == Driver.CHROME:
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            elif driver == Driver.FIREFOX:
                self.driver = webdriver.Firefox()
            elif driver == Driver.EDGE:
                self.driver = webdriver.Edge()
            elif driver == Driver.SAFARI:
                self.driver = webdriver.Safari()
            else:
                raise Exception("Unsupported browser!")
        elif get_platform() == 'win32':
            if driver == Driver.CHROME:
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            elif driver == Driver.FIREFOX:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            elif driver == Driver.EDGE:
                self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            else:
                raise Exception("Unsupported browser!")
        elif get_platform() == 'linux':
            if driver == Driver.CHROME:
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            elif driver == Driver.FIREFOX:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            else:
                raise Exception("Unsupported browser")

    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.quit()
