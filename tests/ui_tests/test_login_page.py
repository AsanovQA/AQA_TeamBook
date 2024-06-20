import os
from dotenv import load_dotenv
import pytest
import allure
from logic.pages.login_page import LoginPage


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
@pytest.mark.regression
def test_login(browser):
    """ Execute login """
    page = LoginPage(browser, os.getenv('URL_LOGIN_PAGE'))
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login_btn()
