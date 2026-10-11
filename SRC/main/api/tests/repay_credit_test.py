# Создание пользователя и проверка валидности имени и пароля
import pytest
from SRC.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Cr


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(self, api_manager: ApiManager, create_account_credit, db_session: Session,
                          create_request_credit):
        repay = api_manager.user_steps.repay_credit(create_request_credit.creditId, create_request_credit.accountId,
                                                    create_request_credit.amount)
        assert repay.amountDeposited == create_request_credit.amount, 'Погасилась вся сумма'

        amount_from_db = Cr.get_credit_by_amount(db_session, repay.amountDeposited)
        assert amount_from_db.amount == repay.amountDeposited, 'Сумма погашения должна совпадать с ответом'

    def test_repay_credit_invalid(self, api_manager: ApiManager, create_account_credit, db_session: Session,
                                  create_request_credit):
        amount_repay = round(create_request_credit.amount / 2, 2)
        api_manager.user_steps.repay_credit_invalid(create_request_credit.creditId,
                                                    create_request_credit.accountId,
                                                    amount_repay)
        amount_from_db = Cr.get_credit_by_amount(db_session, create_request_credit.balance)
        assert amount_from_db.amount is not None, 'Кредит не найден'
