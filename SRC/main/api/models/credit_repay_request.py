from SRC.main.api.models.base_model import BaseModel


# проверка типов данных для создания юзера
class CreditRepayRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float
