import os
import time

import pytest
import requests

from logic.locators.register_page_locators import RegisterPageLocators
from logic.pages.data_ui_negative_registration import RegisterPageData
from logic.pages.register_page import RegisterPage


@pytest.mark.smoke
def test_go_to_register_page(browser):
    """ Go to registration page after opening login page """
    page = RegisterPage(browser, url=os.getenv('LOG_URL'))
    page.open()
    page.go_to_register_page()
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200


def test_registration_with_invalid_email(browser):
    """ Negative: Registration with invalid email """
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_business_email(RegisterPageData.BUSINESS_EMAIL_INVALID)
    page.go_to_organization_name(RegisterPageData.ORGANIZATION_NAME_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_VALID)
    page.go_to_create_org_btn()
    element = page.element_is_visible(RegisterPageLocators.WARNING_MODAL, 1)
    assert element.is_displayed() is True


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
    element = page.element_is_visible(RegisterPageLocators.WARNING_MODAL, 1)
    assert element.is_displayed() is True


def test_registration_with_invalid_password(browser):
    """ Negative: Registration with invalid password """
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_business_email(RegisterPageData.BUSINESS_EMAIL_VALID)
    page.go_to_organization_name(RegisterPageData.ORGANIZATION_NAME_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_INVALID)
    page.go_to_create_org_btn2()
    element = page.element_is_visible(RegisterPageLocators.WARNING_IMG, 2)
    assert element.is_displayed() is True


def test_registration_with_empty_fields(browser):  # падающий тест
    """Negative: Registration with first and last name only"""
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_create_org_btn()
    time.sleep(10)
    element = page.element_is_visible(RegisterPageLocators.WARNING_MODAL, 1)
    assert element.is_displayed() is True


def test_registration_with_empty_one_field(browser):
    """Negative: Registration with one empty field(organization_name)"""
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_business_email(RegisterPageData.BUSINESS_EMAIL_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_VALID)
    page.go_to_create_org_btn()
    element = page.element_is_visible(RegisterPageLocators.WARNING_MODAL, 1)
    assert element.is_displayed() is True


def test_registration_with_existing_mail(browser):
    """Negative: Registration with the existing mail"""
    page = RegisterPage(browser, url=os.getenv('REG_URL'))
    page.open()
    page.go_to_first_name(RegisterPageData.FIRST_NAME_VALID)
    page.go_to_last_name(RegisterPageData.LAST_NAME_VALID)
    page.go_to_business_email(os.getenv('REG_EMAIL'))
    page.go_to_organization_name(RegisterPageData.ORGANIZATION_NAME_VALID)
    page.go_to_password(RegisterPageData.PASSWORD_VALID)
    page.go_to_create_org_btn()
    element = page.element_is_visible(RegisterPageLocators.WARNING_MODAL, 1)
    assert element.is_displayed() is True
