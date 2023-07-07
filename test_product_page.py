import pytest
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# либо "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

url_base = r'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'


def test_add_to_cart(browser):
    page1 = ProductPage(browser, link)
    page1.open()
    page1.add_to_cart_for_test_guest()


@pytest.mark.parametrize('link', [f"{url_base}{i}" for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    if link == f"{url_base}7":
        pytest.xfail(f"Skipping test for link: {link}")
        return
    page2 = ProductPage(browser, link)
    page2.open()
    page2.add_to_cart_for_test_guest()
