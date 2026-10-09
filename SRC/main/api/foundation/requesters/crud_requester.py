import requests
from SRC.main.api.foundation.http_requester import HTTPRequester
from SRC.main.api.models.base_model import BaseModel
from requests import Response
from SRC.main.api.configs.config import Config
import allure


class CrudRequester(HTTPRequester):
    def post(self, model: BaseModel) -> Response:
        body = model.model_dump(by_alias=True) if model is not None else ""
        with allure.step(f"POST {Config.fetch('backendURL')}{self.endpoint.value.url}"):
            allure.attach(str(body), "Request body",
            allure.attachment_type.JSON)

        response = requests.post(
            url=f"{Config.fetch('backendURL')}{self.endpoint.value.url}",
            headers=self.request_spec,
            json=body)
        allure.attach(response.text, "Response body", allure.attachment_type.JSON)
        self.response_spec(response)
        return response
    def delete(self, user_id: int) -> Response:
        response = requests.delete(
            url=f"{Config.fetch('backendURL')}{self.endpoint.value.url}/{user_id}",
            headers=self.request_spec
        )
        self.response_spec(response)
        return response
    def get(self):
        response = requests.get(
            url=f"{Config.fetch('backendURL')}{self.endpoint.value.url}",
            headers=self.request_spec
        )
        self.response_spec(response)
        return response