from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time
import pytest

@pytest.mark.parametrize('offer_number', ['0','1','2','3','4','5','6',pytest.param("7", marks=pytest.mark.xfail),'8','9'])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_name= browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    page.should_be_successfull_message()
    page.successfull_message_contains_product_name(product_name)
    page.should_be_price_in_basket_and_in_message()
    print(link)
    #time.sleep(500)