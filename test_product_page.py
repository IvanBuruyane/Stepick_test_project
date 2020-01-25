from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_name= browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    page.should_be_successfull_message()
    page.successfull_message_contains_product_name(product_name)
    page.should_be_price_in_basket_and_in_message()
    #time.sleep(500)