from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def guest_goes_to_empty_cart(self):
        self.go_to_cart()
        self.expect_cart_to_be_empty()

    def expect_cart_to_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_THE_CART), "Cart is not empty"
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), '"There is no "Your basket is empty" text in the basket"'