import os

import time
import pytest
from urllib3.util import url

from logic.pages.login_page import LoginPage
from utilities.webdriver import WebDriverClass
from utilities.enums import Driver

driver = WebDriverClass(Driver.CHROME).get_driver()


@pytest.fixture(autouse=True)
def browser():
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def execute_login(browser):
    page = LoginPage(browser, os.getenv('URL_LOGIN_PAGE'))
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login_btn()
    time.sleep(1)
    return url
