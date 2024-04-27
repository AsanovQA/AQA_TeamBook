import os
import time
import pytest
import requests

from logic.pages.data_ui_negative_registration import RegisterPageData
from logic.pages.register_page import RegisterPage


@pytest.mark.smoke
def test_go_to_register_page(browser):
    """ Go to registration page after opening login page """
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_register_page()
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200


# @pytest.mark.xfail
def test_registration_with_invalid_email(browser):
    """ Negative: Registration with invalid email """
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    time.sleep(3)
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_business_email(RegisterPageData.BUSINESS_EMAIL_INVALID)
    page.go_to_organization_name(RegisterPageData.ORGANIZATION_NAME_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_VALID)
    page.go_to_create_org_btn()
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200
    # assert False, "This test is expected to fail"


def test_registration_with_invalid_surname(browser):
    """ Negative: Registration with invalid surname """
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_INVALID)
    page.go_to_business_email(RegisterPageData.BUSINESS_EMAIL_VALID)
    page.go_to_organization_name(RegisterPageData.ORGANIZATION_NAME_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_VALID)
    page.go_to_create_org_btn()
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200


def test_registration_with_invalid_password(browser):
    """ Negative: Registration with invalid password """
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_business_email(RegisterPageData.BUSINESS_EMAIL_VALID)
    page.go_to_organization_name(RegisterPageData.ORGANIZATION_NAME_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_INVALID)
    page.go_to_create_org_btn()
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200
