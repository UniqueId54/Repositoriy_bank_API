from SRC.main.api.models.base_model import BaseModel

class User(BaseModel):
    username: str
    role: str
# сверка типов данных ответа на авторизацию юззера
class LoginUserResponse(BaseModel):
    token: str
    user: User









