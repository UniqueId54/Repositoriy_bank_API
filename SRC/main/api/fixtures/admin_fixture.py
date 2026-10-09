import pytest
from SRC.main.api.models.login_user_request import LoginUserRequest


@pytest.fixture
def login_user_request(api_manager):
    user_request = LoginUserRequest(username="admin", password="123456")
    api_manager.admin_steps.login_user(user_request)
    return user_request