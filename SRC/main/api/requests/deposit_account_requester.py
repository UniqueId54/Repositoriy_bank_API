from SRC.main.api.requests.requester import Requester
from SRC.main.api.models.deposit_account_request import DepositAccountRequest
from SRC.main.api.models.deposit_account_response import DepositAccountResponse
import requests
from requests import Response

class DepositAccountRequester(Requester):
    def post(self, deposit_account_request: DepositAccountRequest) -> DepositAccountResponse | Response:
        url = f"{self.base_url}/account/deposit"  # прописываем url с нашей задачей (авторизация юзера)
        response = requests.post(
            url=url,  # адрес куда полетит запрос post
            json=deposit_account_request.model_dump(),  # что мы хотим ввести в тело запроса
            headers=self.headers  # отправка заголовков
        )
        self.response_spec(response)  # проверка статус кода

        if response.status_code == 200:
            return DepositAccountResponse(**response.json())
        return response