from dataclasses import dataclass
#SRC.main.api
from SRC.main.api.models.base_model import BaseModel
from typing import Optional
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_account_response import CreateAccountResponse
from SRC.main.api.models.create_user_response import CreateUserResponse
from enum import Enum
from typing import Type
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.models.create_user_credit_response import CreateUserCreditResponse
from SRC.main.api.models.login_user_request import LoginUserRequest
from SRC.main.api.models.login_user_response import LoginUserResponse
from SRC.main.api.models.deposit_account_request import DepositAccountRequest
from SRC.main.api.models.deposit_account_response import DepositAccountResponse
from SRC.main.api.models.transfer_account_request import TransferAccountRequest
from SRC.main.api.models.transfer_account_response import TransferAccountResponse
from SRC.main.api.models.credit_user_request import CreditUserRequest
from SRC.main.api.models.credit_user_response import CreditUserResponse
from SRC.main.api.models.credit_repay_request import CreditRepayRequest
from SRC.main.api.models.credit_repay_response import CreditRepayResponse




@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        url='/admin/create',
        response_model=CreateUserResponse
    )
    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        url='/admin/users',
        response_model=None
    )
    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        url='/auth/token/login',
        response_model=LoginUserResponse
    )
    CREATE_ACCOUNT = EndpointConfiguration(
        request_model=None,
        url='/account/create',
        response_model=CreateAccountResponse
    )
    DEPOSIT_ACCOUNT = EndpointConfiguration(
        request_model=DepositAccountRequest,
        url='/account/deposit',
        response_model=DepositAccountResponse
    )
    TRANSFER_ACCOUNT = EndpointConfiguration(
        request_model=TransferAccountRequest,
        url='/account/transfer',
        response_model=TransferAccountResponse
    )
    ADMIN_CREATE_USER_CREDIT = EndpointConfiguration(
        request_model=CreateUserCreditRequest,
        url='/admin/create',
        response_model=CreateUserCreditResponse
    )
    REQUEST_CREDIT_USER = EndpointConfiguration(
        request_model=CreditUserRequest,
        url='/credit/request',
        response_model=CreditUserResponse
    )
    REPAY_CREDIT_USER = EndpointConfiguration(
        request_model=CreditRepayRequest,
        url='/credit/repay',
        response_model=CreditRepayResponse
    )
