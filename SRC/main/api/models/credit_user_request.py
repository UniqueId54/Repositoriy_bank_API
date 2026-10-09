from SRC.main.api.models.base_model import BaseModel


# проверка типов данных для создания юзера
class CreditUserRequest(BaseModel):
    accountId: int # id кошелька
    amount: float
    termMonths: int
