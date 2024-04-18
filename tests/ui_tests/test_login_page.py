import os

import pytest
import requests

from logic.pages.login_page import LoginPage


@pytest.mark.smoke
def test_login(browser):
    """ Execute login """
    page = LoginPage(browser, os.getenv('URL_LOGIN_PAGE'))
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login_btn()
    response = requests.get(os.getenv('URL_PLANNING_PAGE'))
    assert response.status_code == 200
