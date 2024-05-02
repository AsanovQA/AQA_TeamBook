import os

from dotenv import load_dotenv
from utilities.settings import ProjectsPageData


load_dotenv()


class ApiData:
    API_BASE_URL = os.environ['API_BASE_URL']

    login_body = {
                'user[email]': os.environ["USER_VALID_EMAIL"],
                'user[password]': os.environ["USER_VALID_PASSWORD"]
            }

    create_project_required_data = {
                'name': f'API{ProjectsPageData.PROJECT_NAME}',
                'code': ProjectsPageData.SHORT_PROJECT_NAME,
                'color': '#EA8FEA',
                'active': True,
                'kind': 'billable'
            }
