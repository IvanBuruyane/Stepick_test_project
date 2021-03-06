from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON);
        add_to_basket_button.click()

    def should_be_successfull_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFULL_MESSAGE),"Alert message isn't displayed"

    def successfull_message_contains_product_name(self,text):
        product_name_in_message=self.browser.find_element(*ProductPageLocators.SUCCESSFULL_MESSAGE).text
        assert product_name_in_message==text,"Alert message is displayed, but with different product name"

    def should_be_price_in_basket_and_in_message(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_message=self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
        assert basket_price_message==product_price, "Basket price isn't equal to product price" #f"{product_price}=={basket_price_message}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFULL_MESSAGE),"Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFULL_MESSAGE), "Success message is presented, but doesn't dissapear"


