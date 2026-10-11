import requests
from requests import Response
from SRC.main.api.models.login_user_request import LoginUserRequest
from SRC.main.api.requests.requester import Requester
from SRC.main.api.models.login_user_response import LoginUserResponse



class LoginUserRequester(Requester):
    def post(self, login_user_request: LoginUserRequest) -> LoginUserRequest | Response:
        url = f"{self.base_url}/auth/token/login" # прописываем url с нашей задачей (авторизация юзера)
        response = requests.post(
            url=url, #адрес куда полетит запрос post
            json=login_user_request.model_dump(),  #что мы хотим ввести в тело запроса
            headers=self.headers  #отправка заголовков
        )
        self.response_spec(response) #проверка статус кода
        return LoginUserResponse(**response.json()) ##возврат нашего класса, с множеством данных результата запроса

    def get(self, login_user_request: LoginUserRequest) -> LoginUserRequest | Response:
        url = f"{self.base_url}/auth/token/login" # прописываем url с нашей задачей (авторизация юзера)
        response = requests.post(
            url=url, #адрес куда полетит запрос post
            json=login_user_request.model_dump(),  #что мы хотим ввести в тело запроса
            headers=self.headers  #отправка заголовков
        )
        self.response_spec(response) #проверка статус кода
        return LoginUserResponse(**response.json()) ##возврат нашего класса, с множеством данных результата запроса























class LoginUserRequester(Requester):
    def post(self, login_user_request: LoginUserRequest) -> LoginUserRequest | Response:
        url = f"{self.base_url}/auth/token/login"
        response = requests.post(
            url=url,
            json=login_user_request.model_dump(),
            headers=self.headers
            )
        self.response_spec(response)
        return LoginUserResponse(**response.json())