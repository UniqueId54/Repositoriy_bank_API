import pytest
from requests import Session
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
#SRC.main.api.
from SRC.main.api.db.crud.account_crud import AccountCrudDb as Acc
from SRC.main.api.fixtures.db_fixture import db_session
from SRC.main.api.classes.api_manager import ApiManager




class TestTransferAccount:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_transfer_account(self, api_manager: ApiManager, create_user_request:CreateUserRequest, db_session:Session):

        api_manager.admin_steps.create_user(create_user_request)
        acc_from = api_manager.user_steps.create_account(create_user_request)
        acc_to = api_manager.user_steps.create_account(create_user_request)
        dep = api_manager.user_steps.deposit_account(acc_from.id, 1000)
        transfer = api_manager.user_steps.transfer_account(acc_from.id, acc_to.id, 500)

        account_from_db = Acc.get_account_by_id(db_session, acc_to.id)
        assert account_from_db.id == acc_to.id, 'Id получаемого кошелька нет в БД'

    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    @pytest.mark.parametrize("amount", [300, 15000])

    def test_transfer_account_invalid(self, api_manager, create_user_request, amount: int, db_session:Session):
        api_manager.admin_steps.create_user(create_user_request)
        acc_from = api_manager.user_steps.create_account(create_user_request)
        acc_to = api_manager.user_steps.create_account(create_user_request)
        api_manager.user_steps.deposit_account(acc_from.id, 1000)
        api_manager.user_steps.transfer_account_invalid(acc_from.id, acc_to.id, amount)

        account_from_db = Acc.get_account_by_id(db_session, acc_to.id)
        assert account_from_db.id == acc_to.id, 'Id получаемого кошелька нет в БД'





