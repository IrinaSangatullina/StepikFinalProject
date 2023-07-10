from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class AddingToCartLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, '.alert-safe:nth-of-type(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_VALUE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    COST_OF_GOOD = (By.CSS_SELECTOR, 'p.price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
