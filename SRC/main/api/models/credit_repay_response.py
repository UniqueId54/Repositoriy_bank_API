from SRC.main.api.models.base_model import BaseModel
from typing import Annotated
from SRC.main.api.generators.creation_rule import CreationRule


# проверка типов данных для создания юзера
class CreditRepayResponse(BaseModel):
    creditId: int
    amountDeposited: Annotated[float, CreationRule(regex=r"^([5-9]\d{3}|1[0-4]\d{3}|15000)$")]
