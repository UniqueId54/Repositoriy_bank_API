from sqlalchemy.orm import Session
from SRC.main.api.db.models.user_table import User


class UserCrudDb:
    @staticmethod  # Чтобы обращаться сразу через класс
    def get_user_by_username(db: Session, username: str) -> User | None:
        return db.query(User).filter_by(username=username).first()



