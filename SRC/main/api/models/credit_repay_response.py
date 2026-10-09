from SRC.main.api.models.base_model import BaseModel


# проверка типов данных для создания юзера
class CreditRepayResponse(BaseModel):
    creditId: int
    amountDeposited: float
