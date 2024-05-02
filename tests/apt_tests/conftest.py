import pytest

from logic.api_client.api_projects import Projects


@pytest.fixture
def projects():
    return Projects()   # Add class in fixture


@pytest.fixture()
def get_token():
    api = Projects()
    token = api.get_token()
    return token
