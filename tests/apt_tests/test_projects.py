import pytest
# from logic.api_client.api_projects import Projects as projects


@pytest.mark.smoke
def test_create_project_with_required_data(projects):
    """Positive: Create a new project with required data"""
    status, project_id = projects.create_project()
    assert status == 201, f'received {status} instead of 201'
    assert project_id is not None
