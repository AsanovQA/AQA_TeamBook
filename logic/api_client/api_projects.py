import json
import os
from dotenv import load_dotenv

import requests

load_dotenv()
API_BASE_URL = os.environ['API_BASE_URL']
VALID_EMAIL = os.environ["USER_VALID_EMAIL"]
VALID_PASSWORD = os.environ["USER_VALID_PASSWORD"]


class Projects:
    """ API library for website https://web.teambooktest.com """

    def __init__(self):
        self.base_url = API_BASE_URL

    def get_token(self) -> json:
        """ Request to site swagger to get a users token using the specified email and password """
        try:
            form_data = {
                'user[email]': VALID_EMAIL,
                'user[password]': VALID_PASSWORD
            }
            res = requests.post(self.base_url + 'auth/login', form_data)
            token = dict(eval(res.text)).get('token')
            status = res.status_code
            return token, status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

