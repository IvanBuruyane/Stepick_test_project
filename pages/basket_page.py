from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_basket_url()
        self.should_not_be_products_in_basket()
        self.should_not_be_proceed_button()

    def should_be_basket_url(self):
        does_basket_exist=self.browser.current_url
        assert does_basket_exist.find("basket")!=-1, f"URL doesn't include 'basket' part, {does_basket_exist}"

    def should_be_empty_basket_message(self):
        self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE),"There is no empty_basket_message on the page"


    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),"There are products in basket"

    def should_not_be_proceed_button(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON),"There is proceed_to_checkout button on the page"
