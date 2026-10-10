from SRC.main.api.db.models.credit_table import Credit
from sqlalchemy.orm import Session



class CreditCrudDb:
    @staticmethod
    def get_credit_by_amount(db: Session, amount: float) -> Credit | None:
        return db.query(Credit).filter_by(amount=amount).first()

    @staticmethod
    def get_credit_by_account_id(db: Session, account_id: int) -> Credit | None:
        return db.query(Credit).filter_by(account_id=account_id).first()

