import os
import time

from logic.locators.projects_page import ProjectsPageLocators
from logic.pages.projects_page import ProjectsPage
from utilities.settings import ProjectsPageData


def create_project(browser):
    """Function to create a new project with all data"""
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
    # page.click_define_start_end_dates_checkbox() # временно не работает сам чек бокс
    page.select_project_color()
    page.add_project_note(note)
    page.click_create_btn()
    page.check_success_message()
    page.go_to_projects_page()
    time.sleep(0.5)
    page.project_added(count)
    return project_name


def archive_project(browser):
    """Function to archive a project """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    project_name = create_project(browser)
    page.fill_search_project_box(project_name)
    count = page.projects_count()
    page.select_project()
    page.click_archive_btn()
    page.click_archive_project_btn_modal()
    page.project_archived(count)
    return project_name


def archive_all_projects(browser):
    """Function to archive all project """
    page = ProjectsPage(browser, os.getenv('URL_PROJECTS_PAGE'))
    page.open()
    create_project(browser)
    page.select_all_projects()
    page.click_archive_btn()
    page.click_archive_project_btn_modal()
    count = page.projects_count()
    assert count == 0, 'Not all projects are archived'
