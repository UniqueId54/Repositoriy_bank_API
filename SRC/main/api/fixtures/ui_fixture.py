import pytest
from playwright.sync_api import sync_playwright, Page, expect
import random

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def generate_phone_number():
    # Генерируем первую цифру (от 1 до 9, чтобы номер не начинался с 0)
    first_digit = str(random.randint(1, 9))
    # Генерируем оставшиеся 9 цифр
    other_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return first_digit + other_digits

@pytest.fixture(scope="function")
def click_button(page):
    return page.locator("#submit")

@pytest.fixture(scope="function")
def auth_standard_user(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.locator('#login-button').click()
    return page


