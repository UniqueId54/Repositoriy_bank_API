import requests
from SRC.main.api.models.create_account_response import CreateAccountResponse
from SRC.main.api.requests.requester import Requester


# наследование от базового класса Requester, где прописана часть url (базовый url) и заголовки
class CreateAccountRequester(Requester):
    def post(self, model=None):
        url = f"{self.base_url}/account/create"
        response = requests.post(
            url=url,
            headers=self.headers
        )
        self.response_spec(response)
        return CreateAccountResponse(**response.json())
