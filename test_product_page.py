import pytest
from .pages.product_page import ProductPage

# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

url_base = r'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart_for_test_guest()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart_for_test_guest()


# def test_add_to_cart(browser):
#     page1 = ProductPage(browser, link)
#     page1.open()
#     page1.add_to_cart_for_test_guest()
#
#
# @pytest.mark.parametrize('link', [f"{url_base}{i}" for i in range(10)])
# def test_guest_can_add_product_to_basket(browser, link):
#     if link == f"{url_base}7":
#         pytest.xfail(f"Skipping test for link: {link}")
#         return
#     page2 = ProductPage(browser, link)
#     page2.open()
#     page2.add_to_cart_for_test_guest()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
