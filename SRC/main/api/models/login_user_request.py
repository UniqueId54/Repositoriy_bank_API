#from pydantic import BaseModel
from SRC.main.api.models.base_model import BaseModel

# сверка типов данных для запроса на авторизацию юззера
class LoginUserRequest(BaseModel):
    username: str
    password: str




