import time

import pytest
import requests

from logic.locators.projects_page import ProjectsPageLocators
from logic.pages.projects_page import ProjectsPage
from logic.pages.settings import ProjectsPageData


@pytest.mark.smoke
def test_go_to_projects_page(browser, execute_login):
    """ Go to project page after logging in """
    page = ProjectsPage(browser, url=execute_login)
    page.go_to_projects_page()
    time.sleep(3)
    response = requests.get(ProjectsPageData.URL_PROJECTS_PAGE)
    assert response.status_code == 200


# @pytest.mark.parametrize('project_name', ProjectsPageData.PROJECT_NAME)
# @pytest.mark.parametrize('short_project_name', ProjectsPageData.SHORT_PROJECT_NAME)
def test_create_project(browser, execute_login):
    """Positive: Create a new project with all required data"""
    project_name = ProjectsPageData.PROJECT_NAME
    short_project_name = ProjectsPageData.SHORT_PROJECT_NAME
    page = ProjectsPage(browser, ProjectsPageData.URL_PROJECTS_PAGE)
    page.open()
    count = page.projects_count()
    page.click_create_project_btn()
    page.fill_project_name(project_name)
    page.fill_short_project_name(short_project_name)
    page.click_create_btn()
    page.check_success_message()
    element = page.element_is_visible(ProjectsPageLocators.SUCCESS_MESSAGE, 3)
    assert element.is_displayed() is True
    page.go_to_projects_page()
    time.sleep(3)
    page.project_added(count)


@pytest.mark.smoke
def test_create_project_with_all_data(browser, execute_login):
    """Positive: Create a new project with all data"""
    project_name = ProjectsPageData.PROJECT_NAME
    short_project_name = ProjectsPageData.SHORT_PROJECT_NAME
    hours = ProjectsPageData.ESTIMATED_HOURS
    business_unit = ProjectsPageData.BUSINESS_UNIT
    note = ProjectsPageData.NOTE
    page = ProjectsPage(browser, ProjectsPageData.URL_PROJECTS_PAGE)
    page.open()
    count = page.projects_count()
    page.click_create_project_btn()
    page.fill_project_name(project_name)
    page.fill_short_project_name(short_project_name)
    page.select_client()
    page.fill_estimated_hours(hours)
    page.select_manager()
    page.select_status()
    page.fill_business_unit(business_unit)
    page.click_define_start_end_dates_checkbox()
    page.select_project_color()
    page.add_project_note(note)
    page.click_create_btn()
    page.check_success_message()
    element = page.element_is_visible(ProjectsPageLocators.SUCCESS_MESSAGE, 3)
    assert element.is_displayed() is True
    page.go_to_projects_page()
    time.sleep(3)
    page.project_added(count)


@pytest.mark.smoke
def test_create_client_with_all_data(browser, execute_login):
    """Positive: Create a new client with all data"""
    client_name = ProjectsPageData.CLIENT_NAME
    client_email = ProjectsPageData.CLIENT_EMAIL
    client_phone = ProjectsPageData.CLIENT_PHONE
    page = ProjectsPage(browser, ProjectsPageData.URL_PROJECTS_PAGE)
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
    time.sleep(3)
    page.client_added(client_count)




