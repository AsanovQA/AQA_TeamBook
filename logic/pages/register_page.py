from .base_page import BasePage
from ..locators.RegisterPageLocators import RegisterPageLocators


class RegisterPage(BasePage):
    def go_to_first_name(self, name):
        first_name = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME)
        first_name.send_keys(name)

    def go_to_last_name(self, surname):
        last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_NAME)
        last_name.send_keys(surname)

    def go_to_business_email(self, business_email):
        biz_email = self.browser.find_element(*RegisterPageLocators.BUSINESS_EMAIL)
        biz_email.send_keys(business_email)

    def go_to_organization_name(self, org_name):
        organization_name = self.browser.find_element(*RegisterPageLocators.REGISTER_ORGANIZATION_NAME)
        organization_name.send_keys(org_name)

    def go_to_password(self, password):
        pswd = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        pswd.send_keys(password)

    def go_to_create_org_btn(self):
        create_org_btn = self.browser.find_element(*RegisterPageLocators.CREATE_ORG_BTN)
        create_org_btn.click()

    def go_to_skip_btn(self):
        skip_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_SKIP_BTN)
        skip_btn.click()

    def go_to_next_btn(self):
        next_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_NEXT_BTN)
        next_btn.click()

    # def enter_project_name(self, prj_name):
    #     project_name = self.browser.find_element(*RegisterPageLocators.REGISTER_PROJECT_NAME)
    #     project_name.send_keys(prj_name)
    #
    # def enter_client_name(self, client_name):
    #     customer_name = self.browser.find_element(*RegisterPageLocators.REGISTER_CLIENT_NAME)
    #     customer_name.send_keys(client_name)
    #
    # def enter_first_user_name(self, first_user_name):
    #     first_employee_name = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_USER_NAME)
    #     first_employee_name.send_keys(first_user_name)
    #
    # def enter_last_user_name(self, user_surname):
    #     last_user_name = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_USER_NAME)
    #     last_user_name.send_keys(user_surname)

    # def enter_user_email(self, user_email):
    #     employee_email = self.browser.find_element(*RegisterPageLocators.REGISTER_USER_EMAIL)
    #     employee_email.send_keys(user_email)
