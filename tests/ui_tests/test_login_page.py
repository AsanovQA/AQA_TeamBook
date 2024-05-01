import os


import pytest

from logic.pages.login_page import LoginPage


@pytest.mark.smoke
def test_login(browser):
    """ Execute login """
    page = LoginPage(browser, os.getenv('URL_LOGIN_PAGE'))
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login_btn()
