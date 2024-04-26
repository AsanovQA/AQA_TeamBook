import os
import time
import pytest
import requests

from logic.locators.register_page_locators import RegisterPageLocators
from logic.pages.register_page import RegisterPage
from tests.ui_tests.data_ui_negative_registration import RegisterPageData


def test_go_to_register_page(browser, register_url):
    page = RegisterPage(browser, url=register_url)
    page.go_to_register_page()
    time.sleep(2)
    response = requests.get(os.getenv('REG_URL'))
    assert response.status_code == 200

