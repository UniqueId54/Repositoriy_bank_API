import pytest
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_user_credit_request import CreateUserCreditRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator


@pytest.fixture
def create_user_request(api_manager):
    user_request = CreateUserRequest(username="Max1c1", password="Pas!sw0rd", role="ROLE_USER")
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
def create_request_credit(api_manager, create_user_credit_request, dep_amount: float):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_request)
    account = api_manager.user_steps.create_account_credit(user_request)
    return api_manager.user_steps.request_credit(account.id, dep_amount, 12)



@pytest.fixture
def account_for_deposit(api_manager):
    user = CreateUserRequest(username="Max121", password="Pas!sw0rd", role="ROLE_USER")
    api_manager.admin_steps.create_user(user)
    account = api_manager.user_steps.create_account(user)
    return account


@pytest.fixture
def two_accounts_to_transfer(api_manager):
    user = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user)
    account_from = api_manager.user_steps.create_account(user)
    account_to = api_manager.user_steps.create_account(user)
    return account_from, account_to


def deposit_accoint_from(api_manager, amount_dep: float):
    user = CreateUserRequest(username="Max151", password="Pas!sw0rd", role="ROLE_USER")
    api_manager.admin_steps.create_user(user)
    account_from = api_manager.user_steps.create_account(user)
    dep_acc = api_manager.user_steps.deposit_account(account_from, amount_dep=amount_dep)
    return dep_acc
