# Создание пользователя и проверка валидности имени и пароля

import pytest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Cr
from SRC.main.api.models.credit_user_request import CreditUserRequest
from SRC.main.api.models.credit_repay_response import CreditRepayResponse


@pytest.mark.api
class TestRepayCredit:
    @pytest.mark.parametrize("credit_amount", [RandomModelGenerator.generate(CreditUserRequest).amount])
    def test_repay_credit(self, api_manager: ApiManager, create_account_credit, db_session: Session,
                          credit_amount: float):
        credit = api_manager.user_steps.request_credit(create_account_credit.id, credit_amount, 12)
        repay = api_manager.user_steps.repay_credit(credit.creditId, credit.accountId,
                                                    credit_amount)
        assert repay.amountDeposited == credit_amount, 'Погасилась вся сумма'

        amount_from_db = Cr.get_credit_by_amount(db_session, repay.amountDeposited)
        assert amount_from_db.amount == repay.amountDeposited, 'Сумма погашения должна совпадать с ответом'

    @pytest.mark.parametrize("credit_amount", [RandomModelGenerator.generate(CreditUserRequest).amount])
    def test_repay_credit_invalid(self, api_manager: ApiManager, create_account_credit, db_session: Session,
                                  credit_amount: float):
        credit = api_manager.user_steps.request_credit(create_account_credit.id, credit_amount, 12)
        amount_repay = round(credit_amount / 2, 2)
        repay = api_manager.user_steps.repay_credit_invalid(credit.creditId, credit.accountId,
                                                            amount_repay)

        amount_from_db = Cr.get_credit_by_amount(db_session, credit.balance)
        assert amount_from_db.amount is not None, 'Кредит не найден'
