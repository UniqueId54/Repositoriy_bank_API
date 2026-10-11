import pytest
from requests import Session
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
# SRC.main.api.
from SRC.main.api.db.crud.account_crud import AccountCrudDb as Acc
from SRC.main.api.fixtures.db_fixture import db_session
from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.models.deposit_account_request import DepositAccountRequest
from SRC.main.api.models.transfer_account_request import TransferAccountRequest


class TestTransferAccount:
    @pytest.mark.parametrize("dep_amount", [RandomModelGenerator.generate(DepositAccountRequest).amount])
    @pytest.mark.parametrize("transfer_amount", [RandomModelGenerator.generate(TransferAccountRequest).amount])
    def test_transfer_account(self, api_manager: ApiManager, deposit_account_from,
                              db_session: Session, dep_amount: float, transfer_amount: float):
        dep, account_to = deposit_account_from
        api_manager.user_steps.transfer_account(dep.id, account_to.id, transfer_amount)

        account_from_db = Acc.get_account_by_id(db_session, account_to.id)
        assert account_from_db.id == account_to.id, 'id аккаунта в БД должен совпадать с API'

    @pytest.mark.parametrize("dep_amount", [RandomModelGenerator.generate(DepositAccountRequest).amount])
    @pytest.mark.parametrize("amount", [300, 15000])
    def test_transfer_account_invalid(self, api_manager: ApiManager,
                                      deposit_account_from,
                                      db_session: Session, dep_amount: float, amount: int):
        dep, account_to = deposit_account_from
        api_manager.user_steps.transfer_account_invalid(dep.id, account_to.id, amount)
        account_from_db = Acc.get_account_by_id(db_session, account_to.id)
        assert account_from_db.id == account_to.id, 'id аккаунта-получателя в БД должен совпадать с API'
