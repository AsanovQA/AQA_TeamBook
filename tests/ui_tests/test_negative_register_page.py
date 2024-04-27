import os
import time
import pytest
import requests

from logic.locators.register_page_locators import RegisterPageLocators
from logic.pages.register_page import RegisterPage
from tests.ui_tests.data_ui_negative_registration import RegisterPageData


@pytest.mark.smoke
def test_go_to_register_page(browser, register_url):
    """ Go to registration page after opening login page """
    page = RegisterPage(browser, url=register_url)
    page.go_to_register_page()
    time.sleep(2)
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200


# def test_registration_with_invalid_email(browser,  register_url):
#     """ Negative: Registration with invalid email """
#     page = RegisterPage(browser, url=register_url)
#     page.open()
#     page.go_to_first_name()
#     page.go_to_last_name()
#     page.go_to_business_email()
#     page.go_to_organization_name()
#     page.go_to_password()
#     page.go_to_create_org_btn()


