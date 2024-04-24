import os
import time

from logic.locators.projects_page import ProjectsPageLocators
from logic.pages.projects_page import ProjectsPage
from utilities.settings import ProjectsPageData


def create_client(browser):
    """Function: Create a new client with all data """
    client_name = ProjectsPageData.CLIENT_NAME
    client_email = ProjectsPageData.CLIENT_EMAIL
    client_phone = ProjectsPageData.CLIENT_PHONE
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    page.click_manage_clients_btn()
    client_count = page.clients_count()
    page.click_new_client_btn()
    page.fill_client_name(client_name)
    page.fill_client_email(client_email)
    page.fill_client_phone(client_phone)
    page.click_save_client_btn()
    page.check_client_success_message()
    element = page.element_is_visible(ProjectsPageLocators.CLIENT_CREATED_SUCCESS_MESSAGE, 3)
    assert element.is_displayed() is True
    time.sleep(1)
    page.client_added(client_count)
    return client_name
