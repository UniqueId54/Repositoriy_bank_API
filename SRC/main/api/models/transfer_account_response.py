from SRC.main.api.models.base_model import BaseModel
from pydantic import Field
class TransferAccountResponse(BaseModel):
    from_acc_id: int = Field(alias="fromAccountId")
    to_acc_id: int = Field(alias="toAccountId")
    from_acc_balance: float = Field(alias="fromAccountIdBalance")
