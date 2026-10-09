from abc import ABC
from typing import Callable
from SRC.main.api.models.base_model import BaseModel


class Requester(ABC):
    def __init__(self, request_spec: dict[str, str], response_spec: Callable):
        self.headers = request_spec
        self.response_spec = response_spec

    def post(self, model: BaseModel): ...
    def get(self): ...


























