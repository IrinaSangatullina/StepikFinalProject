from .base_page import BasePage
from .locators import AddingToCartLocators


class ProductPage(BasePage):
    def add_to_cart_for_test_guest(self):
        login_link = self.browser.find_element(*AddingToCartLocators.ADD_TO_BASKET)
        login_link.click()
        self.solve_quiz_and_get_code()
        self.product_name_matches_the_one_added()
        self.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

    def product_name_matches_the_one_added(self):
        assert self.is_element_present(
            *AddingToCartLocators.ITEM_ADDED_TO_CART), 'Message about adding is not presented'
        message = self.browser.find_element(*AddingToCartLocators.ITEM_ADDED_TO_CART).text
        product_name = self.browser.find_element(*AddingToCartLocators.PRODUCT_NAME).text
        assert product_name == message, 'There is no such product in the message'

    def the_price_of_the_cart_is_the_same_as_the_price_of_the_product(self):
        assert self.is_element_present(*AddingToCartLocators.BASKET_VALUE), 'Cart value not shown'
        basket_value = self.browser.find_element(*AddingToCartLocators.BASKET_VALUE).text
        cost_of_good = self.browser.find_element(*AddingToCartLocators.COST_OF_GOOD).text
        assert cost_of_good == basket_value, 'The price of the cart does not match the price of the product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *AddingToCartLocators.ITEM_ADDED_TO_CART), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *AddingToCartLocators.ITEM_ADDED_TO_CART), 'Success message is still present, but should disappear'

    def add_to_cart_for_test_user(self):
        login_link = self.browser.find_element(*AddingToCartLocators.ADD_TO_BASKET)
        login_link.click()
        self.product_name_matches_the_one_added()
        self.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()
