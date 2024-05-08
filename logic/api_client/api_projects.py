import json

import requests

from logic.api_client.data.body_data import ApiData as AD
from utilities.api_functions.get_token import Token


class Projects:
    """ API library for website https://web.teambooktest.com """

    def __init__(self):
        self.token = Token().get_token()
        self.base_url = AD.API_BASE_URL

    def create_project(self) -> json:
        """Positive: Create a new project with required data"""
        try:
            params = {'token': self.token}
            data = AD.create_project_required_data
            res = requests.post(self.base_url + 'projects', data=data, params=params)
            status = res.status_code
            project_id = res.json().get('id')
            return status, project_id
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def deactivate_project(self, project_id) -> json:
        """Positive: Deactivate a project"""
        try:
            params = {'token': self.token,
                      'project_ids[]': project_id
                      }
            res = requests.patch(self.base_url + 'projects/deactivate', params=params)
            status = res.status_code
            return status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def activate_project(self, project_id) -> json:
        """Positive: Activate a project """
        try:
            params = {
                'token': self.token,
                'project_ids[]': project_id
            }
            res = requests.patch(self.base_url + 'projects/activate', params=params)
            status = res.status_code
            return status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def delete_project(self, project_id) -> json:
        """Positive: Delete a project """
        try:
            params = {
                'token': self.token,
                'project_ids[]': project_id
            }
            res = requests.patch(self.base_url + 'projects/delete', params=params)
            status = res.status_code
            return status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")


# Projects().create_project()
# Projects().get_managers()
# Projects().deactivate_project()
# Projects().activate_project()
# Projects().delete_project()
