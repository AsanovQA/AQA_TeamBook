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
    page.click_define_start_end_dates_checkbox()
    page.select_project_color()
    page.add_project_note(note)
    page.click_create_btn()
    page.check_success_message()
    element = page.element_is_visible(ProjectsPageLocators.SUCCESS_MESSAGE, 3)
    assert element.is_displayed() is True
    page.go_to_projects_page()
    time.sleep(2)
    page.project_added(count)
    return project_name
