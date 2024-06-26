import os

import pytest

from logic.api_client.api_projects import Projects
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
    get_url = driver.current_url
    return get_url


@pytest.fixture
def projects():
    return Projects()   # Add class in fixture


@pytest.fixture()
def get_token():
    api = Projects()
    token = api.get_token()
    return token
