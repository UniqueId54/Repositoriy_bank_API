import pytest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Cr
from SRC.main.api.models.deposit_account_request import DepositAccountRequest
from SRC.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestRequestCredit:
    # утилита-генератор тестовых данных

    @pytest.mark.parametrize("dep_amount",
                             [(RandomModelGenerator.generate(CreditUserRequest).amount)])
    @pytest.mark.parametrize('create_user_credit_request', [RandomModelGenerator.generate(CreateUserCreditRequest)])
    @pytest.mark.parametrize('months', [RandomModelGenerator.generate(CreditUserRequest).termMonths])
    def test_request_credit(self, api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest,
                            db_session: Session, dep_amount: float, create_account_credit, months: int):

        credit = api_manager.user_steps.request_credit(create_account_credit.id, dep_amount, months)
        assert credit.amount == dep_amount, 'Сумма запрошенного кредита должна быть равна заявленной'
        credit_from_db = Cr.get_credit_by_account_id(db_session, credit.accountId)
        assert credit_from_db.account_id == credit.accountId, 'ID кредита в БД должен совпадать с ответом API'

    @pytest.mark.parametrize(
        "create_user_credit_request",
        [RandomModelGenerator.generate(CreateUserCreditRequest)])
    @pytest.mark.parametrize('months', [RandomModelGenerator.generate(CreditUserRequest).termMonths])
    @pytest.mark.parametrize("amount", [1000])
    def test_request_credit_invalid(self, api_manager: ApiManager, amount: int, db_session: Session,
                                    create_user_credit_request: CreateUserCreditRequest,
                                    create_account_credit, months: int):

        cred = api_manager.user_steps.request_credit_invalid(create_account_credit.id, amount, months)
        acc_id_db = Cr.get_credit_by_account_id(db_session, create_account_credit.id)
        assert acc_id_db is None, 'Кредит не должен был создаться'
