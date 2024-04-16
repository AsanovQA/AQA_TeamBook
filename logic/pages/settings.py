from faker import Faker
from datetime import datetime
current_datetime = datetime.now()


class LoginPageData:
    URL_LOGIN_PAGE = 'https://web.teambooktest.com/login'
    USER_VALID_EMAIL = 'anastasiya.niadbailik+teambook@gmail.com'
    USER_VALID_PASSWORD = 'Teambook170468!@'


class PlanningPageData:
    URL_PLANNING_PAGE = 'https://web.teambooktest.com/planners'


class ProjectsPageData:
    URL_PROJECTS_PAGE = 'https://web.teambooktest.com/projects'
    fake = Faker()
    PROJECT_NAME = f'Project {fake.first_name()} AQA '
    SHORT_PROJECT_NAME = f'PAQA {current_datetime.microsecond}'
    NEW_PROJECT_POST = 'https://web.teambooktest.com/api/projects'
    CLIENT_NAME = f'Client {fake.last_name()}'
    CLIENT_EMAIL = f'email{fake.email()}'
    CLIENT_PHONE = '0123456789'
    ESTIMATED_HOURS = '8'
    ESTIMATED_MINUTES = '30'
    BUSINESS_UNIT = 'test unit'
    NOTE = 'Test note'
