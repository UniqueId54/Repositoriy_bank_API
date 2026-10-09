import pytest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Cr


@pytest.mark.api
class TestRequestCredit:
    # утилита-генератор тестовых данных
    @pytest.mark.parametrize(
        "create_user_credit_request",
        [RandomModelGenerator.generate(CreateUserCreditRequest)]
    )
    def test_request_credit(self, api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest,
                            db_session: Session):
        api_manager.admin_steps.create_user_credit(create_user_credit_request)  # регистрация кредитного пользователя
        response = api_manager.user_steps.create_account_credit(
            create_user_credit_request)  # создание счета для кредита
        assert response.balance == 0
        credit = api_manager.user_steps.request_credit(response.id, 5000, 12)
        assert credit.amount == 5000

        credit_from_db = Cr.get_credit_by_id(db_session, credit.accountId)
        assert credit_from_db.account_id == credit.accountId, 'Id кошелька для кредита не попал в БД'



    @pytest.mark.parametrize(
            "create_user_credit_request",
            [RandomModelGenerator.generate(CreateUserCreditRequest)]
        )
    @pytest.mark.parametrize("amount", [1000])

    def test_request_credit_invalid(self, api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest,
                                        amount: int, db_session: Session):
        api_manager.admin_steps.create_user_credit(
                create_user_credit_request)  # регистрация кредитного пользователя
        response = api_manager.user_steps.create_account_credit(
                create_user_credit_request)  # создание счета для кредита
        assert response.balance == 0
        cred = api_manager.user_steps.request_credit_invalid(response.id, amount, 12)


        acc_id_db = Cr.get_credit_account_id(db_session, response.id) is None






