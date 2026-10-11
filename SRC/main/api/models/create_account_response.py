from SRC.main.api.models.base_model import BaseModel

# форма для проверки ответа на запрос создания банк. счета юзером (upd: данных для запроса нет)
class CreateAccountResponse(BaseModel):
    id: int
    number: str
    balance: float
































