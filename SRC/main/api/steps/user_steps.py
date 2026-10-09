from requests import Response
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.specs.request_specs import RequestSpecs
from SRC.main.api.steps.base_steps import BaseSteps
from SRC.main.api.foundation.endpoint import Endpoint
from SRC.main.api.specs.response_specs import ResponseSpecs
from SRC.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from SRC.main.api.models.deposit_account_response import DepositAccountResponse
from SRC.main.api.models.deposit_account_request import DepositAccountRequest
from SRC.main.api.models.transfer_account_request import TransferAccountRequest
from SRC.main.api.models.transfer_account_response import TransferAccountResponse
from SRC.main.api.foundation.requesters.crud_requester import CrudRequester
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.models.credit_user_request import CreditUserRequest
from SRC.main.api.models.credit_repay_request import CreditRepayRequest


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        self.user_headers = RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password)
        account = ValidateCrudRequester(
            self.user_headers,
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(create_user_request)
        return account

    def create_account_credit(self, create_user_credit_request: CreateUserCreditRequest):
        self.user_headers = RequestSpecs.auth_headers(username=create_user_credit_request.username, password=create_user_credit_request.password)
        account = ValidateCrudRequester(
            self.user_headers,
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()).post(create_user_credit_request)
        return account

    def deposit_account(self, account_id: int, amount_dep: float) -> DepositAccountResponse:
        request = DepositAccountRequest(accountId=account_id, amount=amount_dep)
        deposit = ValidateCrudRequester(
            self.user_headers,
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(request)
        return deposit

    def deposit_account_invalid(self, account_id: int, amount: float) -> Response:
        request = DepositAccountRequest(accountId=account_id, amount=amount)
        deposit = CrudRequester(
            self.user_headers,
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(request)
        return deposit

    def transfer_account(self, from_account_id: int, to_account_id: int, amount: float) -> TransferAccountResponse:
        request = TransferAccountRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=amount)
        transfer = ValidateCrudRequester(
            self.user_headers,
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(request)
        return transfer

    def transfer_account_invalid(self, from_account_id: int, to_account_id: int, amount: float) -> TransferAccountResponse:
        request = TransferAccountRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=amount)
        transfer = CrudRequester(
            self.user_headers,
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(request)
        return transfer

    def request_credit(self, accountId: int, amount: float, termMonths: int) -> Response:
        request = CreditUserRequest(accountId=accountId, amount=amount, termMonths=termMonths)
        credit = ValidateCrudRequester(
            self.user_headers,
            Endpoint.REQUEST_CREDIT_USER,
            ResponseSpecs.request_created()
        ).post(request)
        return credit


    def request_credit_invalid(self, id: int, amount: float, termMonths: int) -> Response:
        request = CreditUserRequest(accountId=id, amount=amount, termMonths=termMonths)
        credit = CrudRequester(
            self.user_headers,
            Endpoint.REQUEST_CREDIT_USER,
            ResponseSpecs.request_bad()
        ).post(request)
        return credit

    def repay_credit(self, creditId: int, accountId: int, amount: float) -> Response:
        request = CreditRepayRequest(creditId=creditId, accountId=accountId, amount=amount)
        repay = ValidateCrudRequester(
            self.user_headers,
            Endpoint.REPAY_CREDIT_USER,
            ResponseSpecs.request_ok()
        ).post(request)
        return repay

    def repay_credit_invalid(self, creditId: int, accountId: int, amount: float) -> Response:
        request = CreditRepayRequest(creditId=creditId, accountId=accountId, amount=amount)
        repay = CrudRequester(
            self.user_headers,
            Endpoint.REPAY_CREDIT_USER,
            ResponseSpecs.request_unprocessable()
        ).post(request)
        return repay




