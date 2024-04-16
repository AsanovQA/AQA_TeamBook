import time

import pytest

from logic.pages.login_page import LoginPage
from logic.pages.settings import LoginPageData


@pytest.mark.smoke
def test_login(browser):
    """ Execute login """
    page = LoginPage(browser, LoginPageData.URL_LOGIN_PAGE)
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login_btn()
    time.sleep(3)
