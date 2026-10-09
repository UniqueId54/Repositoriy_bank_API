import pytest
from sqlalchemy.orm import Session
from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.fixtures.db_fixture import db_session
from SRC.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateAccount:
    # вход как админ
    def test_create_account(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0
