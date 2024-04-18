import os

from .base_page import BasePage
from logic.locators.login_page import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(os.environ['USER_VALID_EMAIL'])

    def enter_password(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(os.environ['USER_VALID_PASSWORD'])

    def click_login_btn(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
