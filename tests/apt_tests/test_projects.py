import pytest


@pytest.mark.smoke
def test_create_project_with_required_data(projects):
    """Positive: Create a new project with required data"""
    status, project_id = projects.create_project()
    assert status == 201, f'received {status} instead of 201'
    assert project_id is not None


@pytest.mark.smoke
def test_deactivate_project(projects):
    """Positive: Deactivate a project"""
    project_id = projects.create_project()[1]
    status = projects.deactivate_project(project_id)
    assert status == 200, f'received {status} instead of 200'


@pytest.mark.smoke
def test_activate_project(projects):
    """Positive: Activate a project"""
    project_id = projects.create_project()[1]
    status = projects.activate_project(project_id)
    assert status == 200, f'received {status} instead of 200'


@pytest.mark.smoke
def test_delete_project(projects):
    """Positive: Delete a project"""
    project_id = projects.create_project()[1]
    status = projects.delete_project(project_id)
    assert status == 200, f'received {status} instead of 200'
