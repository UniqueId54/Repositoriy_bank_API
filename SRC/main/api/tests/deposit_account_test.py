import pytest
from sqlalchemy.orm import Session

from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.db.crud.account_crud import AccountCrudDb as Acc

from SRC.main.api.fixtures.db_fixture import db_session
from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.models.deposit_account_request import DepositAccountRequest


# SRC.main.api.
class TestDepositAccount:
    @pytest.mark.parametrize("dep_amount", [RandomModelGenerator.generate(DepositAccountRequest).amount])
    def test_deposit_account(self, api_manager: ApiManager, account_for_deposit,
                             db_session: Session, dep_amount: float):

        dep = api_manager.user_steps.deposit_account(account_for_deposit.id, dep_amount)
        assert dep.balance == dep_amount

        account_from_db = Acc.get_account_by_id(db_session, dep.id)
        assert account_from_db.id == dep.id, 'Id кошелька нет в БД'


    @pytest.mark.parametrize("dep_amount", [RandomModelGenerator.generate(DepositAccountRequest).amount])
    @pytest.mark.parametrize("amount", [500, 10000])
    def test_deposit_account_invalid(self, api_manager: ApiManager, account_for_deposit,
                             db_session: Session, dep_amount: float, amount: int):

        dep = api_manager.user_steps.deposit_account_invalid(account_for_deposit.id, amount)

        account_from_db = Acc.get_account_by_id(db_session, account_for_deposit.id)
        assert account_from_db.balance == 0, 'Баланс нового кошелька не должен быть изменен'
