import time

from .base_page import BasePage, Wait
from logic.locators.projects_page import ProjectsPageLocators


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

    def click_advanced_tab(self):
        self.browser.find_element(*ProjectsPageLocators.ADVANCED_TAB).click()

    def click_add_task_btn(self):
        self.browser.find_element(*ProjectsPageLocators.ADD_TASKS_BTN).click()

    def fill_task_name(self, task_name):
        self.browser.find_element(*ProjectsPageLocators.TASK_NAME).send_keys(task_name)

    def click_save_task_btn(self):
        self.browser.find_element(*ProjectsPageLocators.SAVE_TASK_BTN).click()

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

    def fill_search_project_box(self, project_name):
        # self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD).click()
        self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD).send_keys(project_name)
        time.sleep(2)

    def select_project(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_RECORD_SELECT).click()

    def select_all_projects(self):
        self.browser.find_element(*ProjectsPageLocators.SELECT_ALL_PROJECTS).click()

    def click_archive_btn(self):
        self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN).click()
        time.sleep(2)

    def check_archive_project_modal(self):
        archive_project_modal = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_MODAL)
        assert archive_project_modal, 'Archive project modal is not displayed'

    def click_archive_project_btn_modal(self):
        self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN_MODAL).click()
        time.sleep(1)

    def project_archived(self, count):
        projects = len(self.browser.find_elements(*ProjectsPageLocators.PROJECTS_LIST))
        assert (count - projects) == 1, 'Project is not archived'

    def open_archived_projects(self):
        self.browser.find_element(*ProjectsPageLocators.FILTER_PROJECTS_BY_ACTIVITY).click()
        self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVED_PROJECTS).click()

    def click_archive_project_checkbox(self):
        self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVED_PROJECT_CHECKBOX).click()

    def click_delete_archived_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.DELETE_ARCHIVED_PROJECT_BTN).click()

    def click_delete_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.DELETE_PROJECT_BTN).click()

    def archived_projects_count(self):
        archived_projects = self.browser.find_elements(*ProjectsPageLocators.ARCHIVED_LIST)
        return len(archived_projects)

    def project_deleted(self, archived_count):
        projects = len(self.browser.find_elements(*ProjectsPageLocators.ARCHIVED_LIST))
        assert (archived_count - projects) == 1, 'Project is not deleted'


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
