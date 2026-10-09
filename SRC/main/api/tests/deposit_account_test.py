import pytest
from sqlalchemy.orm import Session

from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.db.crud.account_crud import AccountCrudDb as Acc

from SRC.main.api.fixtures.db_fixture import db_session
from SRC.main.api.classes.api_manager import ApiManager


# SRC.main.api.
class TestDepositAccount:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_deposit_account(self, api_manager: ApiManager, create_user_request:CreateUserRequest, db_session: Session):
        user = api_manager.admin_steps.create_user(create_user_request)
        acc = api_manager.user_steps.create_account(create_user_request)
        dep_amount = 1000
        dep = api_manager.user_steps.deposit_account(acc.id, dep_amount)
        assert dep.balance == 1000

        account_from_db = Acc.get_account_by_id(db_session, dep.id)
        assert account_from_db.id == dep.id, 'Id кошелька нет в БД'


    # прогон входных данных, заведомо ложных, различного характера по условию к проекту
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    @pytest.mark.parametrize("amount", [500, 10000])
    def test_deposit_account_invalid(self, api_manager, create_user_request:CreateUserRequest, amount: int, db_session: Session):
        api_manager.admin_steps.create_user(create_user_request)
        acc_invalid = api_manager.user_steps.create_account(create_user_request)
        dep = api_manager.user_steps.deposit_account_invalid(acc_invalid.id, amount)

        account_from_db = Acc.get_account_by_id(db_session, dep.id)
        assert account_from_db.id == dep.id, 'Id кошелька нет в БД'

