import allure
from ui.pages.basket_page import BasketPage
from playwright.sync_api import Page, expect

class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket = BasketPage(page)

    @allure.step("Переход в корзину через иконку")
    def open_cart(self):
        self.basket.open_cart()
        return self

    @allure.step('Нажать Checkout и перейти на страницу Checkout')
    def checkout(self):
        self.basket.checkout()
        return self

    @allure.step('Удаляем товар по имени')
    def remove_item(self, product_name: str):
        self.basket.remove_item(product_name)
        return self

    @allure.step('Проверяем, что товар присутствует в корзине')
    def expect_item_in_cart(self, product_name: str):
        self.basket.expect_item_in_cart(product_name)
        return self

    @allure.step('Проверяем, что товар отсутствует в корзине')
    def expect_item_not_in_cart(self, product_name: str):
        self.basket.expect_item_not_in_cart(product_name)
        return self

    @allure.step('Возвращает список названий товаров в корзине')
    def get_item_names(self) -> list[str]:
        return self.basket.get_item_names()

    @allure.step('Возвращает список цен всех товаров в корзине')
    def get_item_prices(self) -> list[float]:
        return self.basket.get_item_prices()

    @allure.step('Возвращает общую сумму всех товаров в корзине')
    def get_items_total_price(self) -> float:
        return self.basket.get_items_total_price()

