import json

import requests

from logic.api_client.data.body_data import ApiData as AD
from utilities.regular_functions import reg_token


class Projects:
    """ API library for website https://web.teambooktest.com """

    def __init__(self):
        self.token = None
        self.base_url = AD.API_BASE_URL

    def get_token(self) -> json:
        """ Request to site swagger to get a users token using the specified email and password """
        if self.token:
            return self.token

        try:
            data = AD.login_body
            res = requests.post(self.base_url + 'auth/login', data)
            self.token = reg_token(res.text)
            status = res.status_code
            return self.token, status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def create_project(self) -> json:
        """Positive: Create a new project with required data"""
        try:
            token = self.get_token()[0]
            params = {'token': token}
            data = AD.create_project_required_data
            res = requests.post(self.base_url + 'projects', data=data, params=params)
            status = res.status_code
            project_id = res.json().get('id')
            return status, project_id
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")


# Projects().get_token()
# Projects().create_project()
