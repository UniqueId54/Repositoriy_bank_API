from playwright.sync_api import expect

from ui.pages.login_page import LoginPage
from ui.pages.catalog_page import  CatalogPage
from SRC.main.ui.steps.login_steps import LoginSteps
from SRC.main.ui.steps.catalog_steps import CatalogSteps
from SRC.main.utils.constants import Urls



def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page()
    steps.login(username='standard_user', password='secret_sauce')
    catalog = CatalogPage(page)
    assert catalog.get_products_count() == 0
    expect(page).to_have_url(Urls.INVENTORY)


def test_auth_invalid(page):
    steps = LoginSteps(page)
    steps.open_login_page()
    steps.login(username='locked_out_user', password='secret_sauce')
    expect(page).to_have_url(steps.LOGIN_URL)
    error_text = steps.get_error_text()
    assert "locked out" in error_text

def test_logout(browser, page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)

    login.open_login_page().login("standard_user", "secret_sauce")
    assert catalog.get_products_count() > 0, "Ожидаем, что в каталоге есть товары"

    catalog.logout()
    assert page.url == Urls.BASE, "Ожидаем возврат на страницу логина"

def test_logout_visual_user(browser, page):
    login_page = LoginSteps(page)
    catalog = CatalogSteps(page)
    login_page.open_login_page()
    login_page.login(username='visual_user', password='secret_sauce')
    expect(page).to_have_url(Urls.INVENTORY)
    catalog.logout()
    expect(page).to_have_url(login_page.LOGIN_URL)





