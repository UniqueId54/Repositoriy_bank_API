from typing import Any
import requests
from SRC.main.api.configs.config import Config
from SRC.main.api.models.login_user_request import LoginUserRequest  # models
from SRC.main.api.models.login_user_response import LoginUserResponse  # models

class RequestSpecs:

    @staticmethod
    def base_headers():  # базовые заголовки, для того чтобы не прописывать хедеры в post
        return {
            "Content-Type": "application/json",
            "accept": "application/json",
        }

    @staticmethod
    def auth_headers(username: str, password: str):
        request = LoginUserRequest(username=username, password=password)
        response = requests.post(
            url=f"{Config.fetch("backendURL")}/auth/token/login",  # указываем url куда пойдет запрос
            json=request.model_dump(),  # сериализация в словарь логина и пароля
            headers=RequestSpecs.base_headers()  # вызов верхней функции для хедеров
        )
        if response.status_code == 200:  # проверка на успешность статус кода
            response_data = LoginUserResponse(
                **response.json())  # результат авторизации юзера загоянем в переменную со скелетои модели
            token = response_data.token  # Вызов из тела авторизации юзера его токен
            headers = RequestSpecs.base_headers()  # запихиваем шаблон хедеров
            headers["Authorization"] = f"Bearer {token}"  # в шаблоне хедера добавляем токен юзера
            return headers
        raise Exception(
            f"Failed to login: "
            f"status_code={response.status_code}, "
            f"response={response.text}"
        )
    @staticmethod
    def unauth_headers() -> dict[Any] :
        return RequestSpecs.base_headers()
