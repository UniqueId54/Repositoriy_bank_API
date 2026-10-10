from SRC.main.api.models.base_model import BaseModel
from SRC.main.api.generators.creation_rule import CreationRule
from typing import Annotated


# проверка типов данных для создания юзера
class CreditUserRequest(BaseModel):
    accountId: int # id кошелька
    amount: Annotated[float, CreationRule(regex=r"^([5-9]\d{3}|1[0-4]\d{3}|15000)$")]
    termMonths: int
