# Создание пользователя и проверка валидности имени и пароля

import pytest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Cr

@pytest.mark.api
class TestRepayCredit:
    # утилита-генератор тестовых данных
    @pytest.mark.parametrize(
        "create_user_credit_request",
        [RandomModelGenerator.generate(CreateUserCreditRequest)]
    )
    def test_repay_credit(self, api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest,
                            db_session: Session):
        api_manager.admin_steps.create_user_credit(create_user_credit_request)  # регистрация кредитного пользователя
        response = api_manager.user_steps.create_account_credit(
            create_user_credit_request)  # создание счета для кредита
        assert response.balance == 0
        credit = api_manager.user_steps.request_credit(response.id, 5000, 12)
        repay = api_manager.user_steps.repay_credit(credit.creditId, credit.accountId, credit.amount)
        assert repay.creditId == credit.creditId

        amount_from_db = Cr.get_credit_by_amount(db_session, repay.amountDeposited)
        assert amount_from_db.amount == repay.amountDeposited, 'Сумма погашения не внеслась в БД'

    @pytest.mark.parametrize(
            "create_user_credit_request",
            [RandomModelGenerator.generate(CreateUserCreditRequest)]
        )
    @pytest.mark.parametrize("amount, amount_repay", [(5000, 3000)]) # негативные тестовые данные, когда сумма погашен

    def test_repay_credit_invalid(self, api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest,
                                        amount: int, amount_repay: int, db_session: Session):
        api_manager.admin_steps.create_user_credit(
                create_user_credit_request)  # регистрация кредитного пользователя
        response = api_manager.user_steps.create_account_credit(
                create_user_credit_request)  # создание счета для кредита
        assert response.balance == 0
        credit = api_manager.user_steps.request_credit(response.id, amount, 12)
        api_manager.user_steps.repay_credit_invalid(credit.creditId, credit.accountId, amount_repay)

        acc_id_db = Cr.get_credit_account_id(db_session, credit.accountId)
        assert acc_id_db.account_id == credit.accountId, 'ID кошелька не внесен в БД'




