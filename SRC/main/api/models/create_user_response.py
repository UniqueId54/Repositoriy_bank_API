from SRC.main.api.models.base_model import BaseModel


# сверка типов данных ответа на создание юзера
class CreateUserResponse(BaseModel):
    id: int
    username: str
    password: str
    role: str



