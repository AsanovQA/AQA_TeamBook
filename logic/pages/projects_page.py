import time

from logic.core.waiters import WaitElement as wait
from logic.locators.projects_page import ProjectsPageLocators
from .base_page import BasePage


class ProjectsPage(BasePage):
    def go_to_projects_page(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECTS_TAB).click()
        wait.wait_until_element_be_visible(self.browser, ProjectsPageLocators.CREATE_PROJECT_BTN)

    """Project functions"""

    def click_create_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CREATE_PROJECT_BTN).click()
        wait.wait_until_element_be_visible(self.browser, ProjectsPageLocators.CREATE_BTN)

    def fill_project_name(self, project_name):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME).send_keys(project_name)

    def fill_short_project_name(self, short_project_name):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME).send_keys(short_project_name)

    def select_client(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_FIELD).click()
        time.sleep(0.5)
        self.browser.find_element(*ProjectsPageLocators.SELECT_CLIENT).click()

    def fill_estimated_hours(self, hours):
        self.browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS).send_keys(hours)

    def select_manager(self):
        self.browser.find_element(*ProjectsPageLocators.MANAGER).click()
        self.browser.find_element(*ProjectsPageLocators.SELECT_MANAGER).click()

    def select_status(self):
        self.browser.find_element(*ProjectsPageLocators.STATUS).click()
        self.browser.find_element(*ProjectsPageLocators.SELECT_STATUS).click()

    def fill_business_unit(self, business_unit):
        self.browser.find_element(*ProjectsPageLocators.BUSINESS_UNIT).send_keys(business_unit)

    def click_define_start_end_dates_checkbox(self):
        self.browser.find_element(*ProjectsPageLocators.DEFINE_START_CHECKBOX).click()
        time.sleep(0.5)
        self.browser.find_element(*ProjectsPageLocators.DEFINE_END_CHECKBOX).click()

    def click_project_color(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR).click()

    def select_project_color(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR).click()
        self.browser.find_element(*ProjectsPageLocators.SELECT_PROJECT_COLOR).click()

    def add_project_note(self, note):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NOTES).click()
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NOTES).send_keys(note)

    def click_create_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CREATE_BTN).click()
        wait.wait_until_element_be_visible(self.browser, ProjectsPageLocators.SUCCESS_MESSAGE)

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
        wait.wait_until_element_be_visible(self.browser, ProjectsPageLocators.PROJECT_RECORD_CHECKBOX)
        projects = len(self.browser.find_elements(*ProjectsPageLocators.PROJECTS_LIST))
        assert (projects - count) == 1, 'Project is not added'

    def project_is_not_added(self, count):
        projects = len(self.browser.find_elements(*ProjectsPageLocators.PROJECTS_LIST))
        assert (projects - count) == 0, "but was{0}".format((projects - count).__str__())

    def fill_search_project_box(self, project_name):
        self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD).send_keys(project_name)
        # time.sleep(0.5)

    def clear_search_project_box(self):
        self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD).clear()
        # time.sleep(0.5)

    def select_project(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_RECORD_CHECKBOX).click()

    def select_all_projects(self):
        self.browser.find_element(*ProjectsPageLocators.SELECT_ALL_PROJECTS).click()

    def click_archive_btn(self):
        self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN).click()
        time.sleep(0.5)

    def check_archive_project_modal(self):
        archive_project_modal = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_MODAL)
        assert archive_project_modal, 'Archive project modal is not displayed'

    def click_archive_project_btn_modal(self):
        self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN_MODAL).click()
        time.sleep(0.5)

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

    def click_activate_archived_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.ACTIVATE_ARCHIVED_PROJECT_BTN).click()

    def click_reactivate_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.REACTIVATE_PROJECT_BTN).click()

    def project_activated(self, archived_count):
        projects = len(self.browser.find_elements(*ProjectsPageLocators.ARCHIVED_LIST))
        assert (archived_count - projects) == 1, 'Project is not activated'

    def open_projects_info(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_RECORD).click()

    def click_edit_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.EDIT_PROJECT_BTN).click()

    def clear_project_name_field(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME_EDIT).clear()

    def edit_project_name(self, new_project_name):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME_EDIT).send_keys(new_project_name)

    def clear_project_short_name_field(self):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME_EDIT).clear()

    def edit_short_project_name(self, new_short_name):
        self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME_EDIT).send_keys(new_short_name)

    def click_save_updated_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.SAVE_UPDATED_PROJECT_BTN).click()

    def click_export_project_btn(self):
        self.browser.find_element(*ProjectsPageLocators.EXPORT_PROJECT_BTN).click()

    """Client Functions"""

    def click_manage_clients_btn(self):
        self.browser.find_element(*ProjectsPageLocators.MANAGE_CLIENTS_BTN).click()

    def click_new_client_btn(self):
        self.browser.find_element(*ProjectsPageLocators.NEW_CLIENT_BTN).click()

    def fill_client_name(self, client_name):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_NAME).send_keys(client_name)

    def clear_client_name_field(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_NAME).clear()

    def edit_client_name(self, new_client_name):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_NAME).send_keys(new_client_name)

    def fill_client_email(self, client_email):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_EMAIL).send_keys(client_email)

    def clear_client_email_field(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_EMAIL).clear()

    def edit_client_email(self, new_client_email):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_EMAIL).send_keys(new_client_email)

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

    def fill_client_search_box(self, client_name):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_SEARCH_BOX).send_keys(client_name)

    def clear_client_search_box(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_SEARCH_BOX).clear()

    def click_edit_client_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_EDIT_BTN).click()

    def click_save_updated_client_btn(self):
        self.browser.find_element(*ProjectsPageLocators.SAVE_UPDATED_CLIENT_BTN).click()

    def click_client_delete_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_DELETE_BTN).click()

    def click_client_confirm_delete_btn(self):
        self.browser.find_element(*ProjectsPageLocators.CLIENT_CONFIRM_DELETE_BTN).click()

    def client_deleted(self, count):
        clients = len(self.browser.find_elements(*ProjectsPageLocators.CLIENT_LIST))
        assert (count - clients) == 1, 'Client is not deleted'

    def check_client_updated_success_message(self):
        client_success_message = self.browser.find_element(*ProjectsPageLocators.CLIENT_SUCCESS_MESSAGE)
        assert client_success_message
