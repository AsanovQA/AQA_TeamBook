import os
import time

import pytest
import requests

from logic.locators.projects_page import ProjectsPageLocators
from logic.pages.projects_page import ProjectsPage
from utilities.projects_page.clients import create_client
from utilities.settings import ProjectsPageData
from utilities.projects_page.projects import create_project, archive_all_projects, archive_project


@pytest.mark.smoke
def test_go_to_projects_page(browser, execute_login):
    """ Go to project page after logging in """
    page = ProjectsPage(browser, url=execute_login)
    page.go_to_projects_page()
    response = requests.get(os.getenv('URL_PROJECTS_PAGE'))
    assert response.status_code == 200


@pytest.mark.smoke
def test_create_client_with_all_data(browser, execute_login):
    """Positive: Create a new client with all data """
    create_client(browser)


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
    page.go_to_projects_page()
    time.sleep(0.5)
    page.project_added(count)


@pytest.mark.smoke
def test_create_project_with_all_data(browser, execute_login):
    """Positive: Create a new project with all data"""
    create_project(browser)


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
    # page.click_define_start_end_dates_checkbox() #временно не работает чек бокс
    page.select_project_color()
    page.add_project_note(note)
    page.click_advanced_tab()
    page.click_add_task_btn()
    page.fill_task_name(task_name)
    page.click_save_task_btn()
    page.click_create_btn()
    page.check_success_message()
    element = page.element_is_visible(ProjectsPageLocators.SUCCESS_MESSAGE, 1)
    assert element.is_displayed() is True
    page.go_to_projects_page()
    time.sleep(0.5)
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
    project_name = archive_project(browser)
    page.open_archived_projects()
    page.fill_search_project_box(project_name)
    archived_count = page.archived_projects_count()
    page.click_archive_project_checkbox()
    page.click_delete_archived_project_btn()
    page.click_delete_project_btn()
    time.sleep(1)
    page.project_deleted(archived_count)


@pytest.mark.regression
def test_delete_all_projects(browser, execute_login):
    """Positive: Delete all projects """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    archive_all_projects(browser)
    page.open_archived_projects()
    page.select_all_projects()
    page.click_delete_archived_project_btn()
    page.click_delete_project_btn()
    time.sleep(1)
    count = page.projects_count()
    assert count == 0, 'Not all projects are deleted'


@pytest.mark.smoke
def test_activate_archived_project(browser, execute_login):
    """Positive: Activate an archived project """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = archive_project(browser)
    page.open_archived_projects()
    page.fill_search_project_box(project_name)
    archived_count = page.archived_projects_count()
    page.click_archive_project_checkbox()
    page.click_activate_archived_project_btn()
    page.click_reactivate_project_btn()
    time.sleep(0.5)
    page.project_activated(archived_count)


@pytest.mark.regression
def test_activate_all_archived_project(browser, execute_login):
    """Positive: Activate an archived project """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    archive_all_projects(browser)
    page.open_archived_projects()
    archived_count = page.archived_projects_count()
    page.select_all_projects()
    page.click_activate_archived_project_btn()
    page.click_reactivate_project_btn()
    time.sleep(0.5)
    page.project_activated(archived_count)


@pytest.mark.smoke
def test_add_task_to_project(browser, execute_login):
    """Positive: Add a new tak to a project"""
    task_name = ProjectsPageData.TASK_NAME
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = create_project(browser)
    page.fill_search_project_box(project_name)
    page.open_projects_info()
    page.click_edit_project_btn()
    page.click_advanced_tab()
    page.click_add_task_btn()
    page.fill_task_name(task_name)
    page.click_save_task_btn()
    page.click_save_updated_project_btn()
    page.check_success_message()
    element = page.element_is_visible(ProjectsPageLocators.SUCCESS_MESSAGE, 1)
    assert element.is_displayed() is True


@pytest.mark.smoke
def test_export_project(browser, execute_login):
    """Positive: Export a project"""
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = create_project(browser)
    page.fill_search_project_box(project_name)
    page.select_project()
    page.click_export_project_btn()


@pytest.mark.smoke
def test_edit_project(browser, execute_login):
    """Positive: Edit a project """
    new_project_name = ' new'
    new_short_name = ' new'
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = create_project(browser)
    page.fill_search_project_box(project_name)
    page.open_projects_info()
    page.click_edit_project_btn()
    page.clear_project_name_field()
    time.sleep(0.5)
    page.edit_project_name(new_project_name)
    time.sleep(0.5)
    page.clear_project_short_name_field()
    page.edit_short_project_name(new_short_name)
    page.click_save_updated_project_btn()
    page.check_success_message()
    page.clear_search_project_box()
    page.fill_search_project_box(f'{project_name} new')
    count = page.projects_count()
    assert count == 1, 'Project is not edited'


@pytest.mark.smoke
def test_edit_client(browser, execute_login):
    """Positive: Edit a client """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    client_name = create_client(browser)
    new_client_name = f'{client_name} new'
    new_client_email = 'newclient@test.com'
    page.fill_client_search_box(client_name)
    page.click_edit_client_btn()
    page.clear_client_name_field()
    page.edit_client_name(new_client_name)
    page.clear_client_email_field()
    page.edit_client_email(new_client_email)
    page.click_save_updated_client_btn()
    page.check_client_updated_success_message()
    page.clear_client_search_box()
    page.fill_client_search_box(f'{client_name} new')
    count = page.clients_count()
    assert count == 1, 'Updated client is not found'


@pytest.mark.smoke
def test_delete_client(browser, execute_login):
    """Positive: Delete a client """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    client_name = create_client(browser)
    page.fill_client_search_box(client_name)
    client_count = page.clients_count()
    page.click_client_delete_btn()
    page.click_client_confirm_delete_btn()
    element = page.element_is_visible(ProjectsPageLocators.CLIENT_CREATED_SUCCESS_MESSAGE, 3)
    assert element.is_displayed() is True
    time.sleep(0.5)
    page.client_deleted(client_count)
