from faker import Faker
from datetime import datetime


current_datetime = datetime.now()


class ProjectsPageData:
    fake = Faker()
    PROJECT_NAME = f'Project {fake.first_name()} AQA '
    SHORT_PROJECT_NAME = f'PAQA {current_datetime.microsecond}'
    CLIENT_NAME = f'Client {fake.last_name()}'
    CLIENT_EMAIL = f'email{fake.email()}'
    CLIENT_PHONE = '0123456789'
    ESTIMATED_HOURS = '8'
    ESTIMATED_MINUTES = '30'
    BUSINESS_UNIT = 'test unit'
    NOTE = 'Test note'
