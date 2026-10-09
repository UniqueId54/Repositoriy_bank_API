from typing import Optional, Any
import allure
from SRC.main.api.foundation.http_requester import HTTPRequester
from SRC.main.api.foundation.requesters.crud_requester import CrudRequester
from SRC.main.api.models.base_model import BaseModel
from SRC.main.api.configs.config import Config


# валидация моделей с данными из response
class ValidateCrudRequester(HTTPRequester):
    def __init__(self, request_spec, endpoint, response_spec):
        super().__init__(request_spec, endpoint, response_spec)
        self.crud_requester = CrudRequester(
            request_spec=self.request_spec,
            endpoint=self.endpoint,
            response_spec=self.response_spec
        )
    def post(self, model: Optional[BaseModel] = None) -> Optional[Any]:
        response = self.crud_requester.post(model)
        with allure.step(f"POST {Config.fetch('backendURL')}{self.endpoint.value.url} and Validated Model"):
            allure.attach(f"Validated Model response: {self.endpoint.value.response_model.__name__}")

        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())

    def delete(self, user_id: int):
        response = self.crud_requester.delete(user_id)
        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())
    def get(self):
        response=self.crud_requester.get()
        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())