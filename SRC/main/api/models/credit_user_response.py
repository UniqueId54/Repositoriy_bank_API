from pydantic import Field, ConfigDict



from SRC.main.api.models.base_model import BaseModel


# проверка типов данных для создания юзера
class CreditUserResponse(BaseModel):
    accountId: int = Field(alias='id')
    amount: float
    termMonths: int
    balance: float
    creditId: int

    model_config = ConfigDict(populate_by_name=True)
