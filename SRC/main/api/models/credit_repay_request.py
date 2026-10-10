from typing import Annotated
from SRC.main.api.generators.creation_rule import CreationRule
from SRC.main.api.models.base_model import BaseModel


# проверка типов данных для создания юзера
class CreditRepayRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float