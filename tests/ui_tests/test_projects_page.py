import os
import time

import pytest
import requests

from logic.locators.projects_page import ProjectsPageLocators
from logic.pages.projects_page import ProjectsPage
from utilities.settings import ProjectsPageData
from utilities.projects_page.projects import create_project


@pytest.mark.smoke
def test_go_to_projects_page(browser, execute_login):
    """ Go to project page after logging in """
    page = ProjectsPage(browser, url=execute_login)
    page.go_to_projects_page()
    time.sleep(3)
    response = requests.get(os.getenv('URL_PROJECTS_PAGE'))
    assert response.status_code == 200


def test_create_project(browser, execute_login):
    """Positive: Create a new project with all required data"""
    project_name = ProjectsPageData.PROJECT_NAME
    short_project_name = ProjectsPageData.SHORT_PROJECT_NAME
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
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
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
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


@pytest.mark.regression
def test_project_with_task(browser, execute_login):
    """Positive: Create a new project with task"""
    task_name = ProjectsPageData.TASK_NAME
    project_name = ProjectsPageData.PROJECT_NAME
    short_project_name = ProjectsPageData.SHORT_PROJECT_NAME
    hours = ProjectsPageData.ESTIMATED_HOURS
    business_unit = ProjectsPageData.BUSINESS_UNIT
    note = ProjectsPageData.NOTE
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
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
    page.click_advanced_tab()
    page.click_add_task_btn()
    page.fill_task_name(task_name)
    page.click_save_task_btn()
    page.click_create_btn()
    page.check_success_message()
    element = page.element_is_visible(ProjectsPageLocators.SUCCESS_MESSAGE, 3)
    assert element.is_displayed() is True
    page.go_to_projects_page()
    time.sleep(3)
    page.project_added(count)


@pytest.mark.smoke
def test_archive_project(browser, execute_login):
    """Positive: Archive a project """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = create_project(browser)
    page.fill_search_project_box(project_name)
    count = page.projects_count()
    page.select_project()
    page.click_archive_btn()
    page.click_archive_project_btn_modal()
    page.project_archived(count)


@pytest.mark.regression
def test_archive_all_projects(browser, execute_login):
    """Positive: Archive all projects """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    create_project(browser)
    page.select_all_projects()
    page.click_archive_btn()
    page.click_archive_project_btn_modal()
    count = page.projects_count()
    assert count == 0, 'Not all projects are archived'


@pytest.mark.smoke
def test_delete_project(browser, execute_login):
    """Positive: Delete a project """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = create_project(browser)
    page.fill_search_project_box(project_name)
    count = page.projects_count()
    page.select_project()
    page.click_archive_btn()
    page.click_archive_project_btn_modal()
    page.project_archived(count)
    page.open_archived_projects()
    page.fill_search_project_box(project_name)
    archived_count = page.archived_projects_count()
    page.click_archive_project_checkbox()
    page.click_delete_archived_project_btn()
    page.click_delete_project_btn()
    time.sleep(2)
    page.project_deleted(archived_count)


@pytest.mark.regression
def test_delete_all_projects(browser, execute_login):
    """Positive: Delete all projects """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    create_project(browser)
    page.open_archived_projects()
    archived_count = page.archived_projects_count()
    page.select_all_projects()
    page.click_delete_archived_project_btn()
    page.click_delete_project_btn()
    time.sleep(2)
    page.project_deleted(archived_count)


# def




@pytest.mark.smoke
def test_create_client_with_all_data(browser, execute_login):
    """Positive: Create a new client with all data """
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
    time.sleep(3)
    page.client_added(client_count)
