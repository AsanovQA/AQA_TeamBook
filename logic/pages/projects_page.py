import requests
import time

from .base_page import BasePage
from logic.locators.projects_page import ProjectsPageLocators
from .settings import ProjectsPageData


class ProjectsPage(BasePage):
    def go_to_projects_page(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECTS_TAB).click()

    """Project functions"""

    def click_create_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CREATE_PROJECT_BTN).click()

    def fill_project_name(self, project_name):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME).send_keys(project_name)

    def fill_short_project_name(self, short_project_name):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME).send_keys(short_project_name)

    def select_client(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_FIELD).click()
        time.sleep(1)
        self.browser.find_element(*ProjectsPageLocators.SELECT_CLIENT).click()

    def fill_estimated_hours(self, hours):
        self.browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS).send_keys(hours)

    def select_manager(self):
        self.browser.find_element(*ProjectsPageLocators.MANAGER).click()
        time.sleep(1)
        self.browser.find_element(*ProjectsPageLocators.SELECT_MANAGER).click()

    def select_status(self):
        self.browser.find_element(*ProjectsPageLocators.STATUS).click()
        time.sleep(1)
        self.browser.find_element(*ProjectsPageLocators.SELECT_STATUS).click()

    def fill_business_unit(self, business_unit):
        self.browser.find_element(*ProjectsPageLocators.BUSINESS_UNIT).send_keys(business_unit)

    def click_define_start_end_dates_checkbox(self):
        self.browser.find_element(*ProjectsPageLocators.DEFINE_START_CHECKBOX).click()
        time.sleep(1)
        self.browser.find_element(*ProjectsPageLocators.DEFINE_END_CHECKBOX).click()

    def click_project_color(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR).click()

    def select_project_color(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR).click()
        time.sleep(1)
        self.browser.find_element(*ProjectsPageLocators.SELECT_PROJECT_COLOR).click()

    def add_project_note(self, note):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NOTES).click()
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NOTES).send_keys(note)

    def click_create_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CREATE_BTN).click()

    def check_success_message(self):
        success_message = self.browser.find_element(*ProjectsPageLocators.SUCCESS_MESSAGE)
        assert success_message

    def projects_count(self):
        projects = self.browser.find_elements(*ProjectsPageLocators.PROJECTS_LIST)
        return len(projects)

    def project_added(self, count):
        projects = len(self.browser.find_elements(*ProjectsPageLocators.PROJECTS_LIST))
        assert (projects - count) == 1, 'Project is not added'

    def project_is_not_added(self, count):
        projects = len(self.browser.find_elements(*ProjectsPageLocators.PROJECTS_LIST))
        assert (projects - count) == 0, "but was{0}".format((projects - count).__str__())

    """Client Functions"""
    def click_manage_clients_btn(self):
        self.browser.find_element(*ProjectsPageLocators.MANAGE_CLIENTS_BTN).click()

    def click_new_client_btn(self):
        self.browser.find_element(*ProjectsPageLocators.NEW_CLIENT_BTN).click()

    def fill_client_name(self, client_name):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_NAME).send_keys(client_name)

    def fill_client_email(self, client_email):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_EMAIL).send_keys(client_email)

    def fill_client_phone(self, client_phone):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_PHONE).send_keys(client_phone)

    def click_save_client_btn(self):
        self.browser.find_element(*ProjectsPageLocators.SAVE_CLIENT_BTN).click()

    def check_client_success_message(self):
        client_success_message = self.browser.find_element(*ProjectsPageLocators.CLIENT_CREATED_SUCCESS_MESSAGE)
        assert client_success_message

    def clients_count(self):
        clients = self.browser.find_elements(*ProjectsPageLocators.CLIENT_LIST)
        return len(clients)

    def client_added(self, count):
        clients = len(self.browser.find_elements(*ProjectsPageLocators.CLIENT_LIST))
        assert (clients - count) == 1, 'Client is not added'

    def client_is_not_added(self, count):
        clients = len(self.browser.find_elements(*ProjectsPageLocators.CLIENT_LIST))
        assert (clients - count) == 0, "but was{0}".format((clients - count).__str__())