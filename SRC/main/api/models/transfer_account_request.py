from SRC.main.api.models.base_model import BaseModel
from typing import Annotated
from SRC.main.api.generators.creation_rule import CreationRule
from SRC.main.api.models.credit_user_request import CreditUserRequest

from pydantic import Field

class TransferAccountRequest(BaseModel):
    from_account_id: int = Field(alias="fromAccountId")
    to_account_id: int = Field(alias="toAccountId")
    amount: Annotated[int, CreationRule(min_value=500, max_value=10000)]
