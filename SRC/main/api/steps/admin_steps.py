from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from SRC.main.api.specs.request_specs import RequestSpecs
from SRC.main.api.specs.response_specs import ResponseSpecs
from SRC.main.api.foundation.endpoint import Endpoint
from SRC.main.api.foundation.requesters.crud_requester import CrudRequester
from SRC.main.api.steps.base_steps import BaseSteps
from SRC.main.api.models.login_user_request import LoginUserRequest


class AdminSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
        RequestSpecs.auth_headers(username='admin', password='123456'),
        Endpoint.ADMIN_CREATE_USER,
        ResponseSpecs.request_ok()
        ).post(create_user_request)
        self.created_obj.append(response)
        return response

    def delete_user(self, user_id: int):
        CrudRequester(
            RequestSpecs.auth_headers(username='admin', password='123456'),
            Endpoint.ADMIN_DELETE_USER,
            ResponseSpecs.request_ok()
        ).delete(user_id)

    def create_invalid_user(self, create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username='admin', password='123456'),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.request_bad()
        ).post(create_user_request)

    def login_user(self, login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response

    def login_user_credit(self, login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response

    def create_user_credit(self, create_user_credit_request: CreateUserCreditRequest):
        response = ValidateCrudRequester(
        RequestSpecs.auth_headers(username='admin', password='123456'),
        Endpoint.ADMIN_CREATE_USER_CREDIT,
        ResponseSpecs.request_ok()
        ).post(create_user_credit_request)
        self.created_obj.append(response)
        return response




