from typing import Protocol
from requests import Response
from SRC.main.api.models.base_model import BaseModel


class CrudEndpoint(Protocol):
    def post(self, model: BaseModel) -> BaseModel | Response:...
    def get(self) -> BaseModel | Response:...
    def delete(self, user_id: int) -> BaseModel | Response:...



