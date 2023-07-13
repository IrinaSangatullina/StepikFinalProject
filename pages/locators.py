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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')


class BasketPageLocators:
    VIEW_CART = (By.CSS_SELECTOR, '#default header > div:nth-child(1) > div > div:nth-child(2) > span > a')
    PRODUCTS_IN_THE_CART = (By.CSS_SELECTOR, '#content_inner > div:nth-child(1) > div > h2')
    BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
