import requests
from requests import Response
from SRC.main.api.requests.requester import Requester
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_user_response import CreateUserResponse
from SRC.main.api.configs.config import Config


# Формирует запросы на создание пользователя(можно не прописывать каждый раз авторизацию админа)
class CreateUserRequester(Requester):
    def post(self, create_user_request: CreateUserRequest) -> CreateUserResponse | Response:
        url = f"{Config.fetch('backendURL')}/admin/create"
        response = requests.post(
            url=url,
            json=create_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return CreateUserResponse(**response.json())


