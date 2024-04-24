import os
import time

import pytest
import requests
from selenium.webdriver.support.wait import WebDriverWait

from logic.locators.login_page import LoginPageLocators
from logic.locators.projects_page import ProjectsPageLocators
from logic.pages.login_page import LoginPage


@pytest.mark.smoke
def test_login(browser):
    """ Execute login """
    page = LoginPage(browser, os.getenv('URL_LOGIN_PAGE'))
    page.open()
    page.enter_email()
    time.sleep(10)
    page.enter_password()
    page.click_login_btn()
