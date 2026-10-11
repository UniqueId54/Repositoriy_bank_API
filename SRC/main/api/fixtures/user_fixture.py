import pytest
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.models.deposit_account_request import DepositAccountRequest
from SRC.main.api.models.credit_user_request import CreditUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_user_credit_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user_credit(user_request)
    return user_request


@pytest.fixture
def create_account_credit(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user_credit(user_request)
    account = api_manager.user_steps.create_account_credit(user_request)
    return account

@pytest.fixture
def create_request_credit(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_request)
    account = api_manager.user_steps.create_account_credit(user_request)
    months = RandomModelGenerator.generate(CreditUserRequest).termMonths
    dep_amount = RandomModelGenerator.generate(DepositAccountRequest).amount
    cred = api_manager.user_steps.request_credit(account.id, dep_amount, months)
    return cred

@pytest.fixture
def account_for_deposit(api_manager):
    user = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user)
    account = api_manager.user_steps.create_account(user)
    return account

@pytest.fixture
def deposit_account_from(api_manager):
    user = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user)
    account_from = api_manager.user_steps.create_account(user)
    account_to = api_manager.user_steps.create_account(user)
    dep_amount = RandomModelGenerator.generate(DepositAccountRequest).amount
    dep = api_manager.user_steps.deposit_account(account_from.id, dep_amount)
    return dep, account_to

@pytest.fixture
def request_credit(api_manager):
    user = RandomModelGenerator.generate(CreateUserRequest)




