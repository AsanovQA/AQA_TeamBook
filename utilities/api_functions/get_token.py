import json

import requests

from logic.api_client.data.body_data import ApiData as AD
from utilities.regular_functions import reg_token


class Token:
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
            return self.token
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")


# Token().get_token()
