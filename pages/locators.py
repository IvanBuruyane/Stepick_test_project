from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON= (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL=(By.CSS_SELECTOR,"#id_registration-email")
    REGISTRATION_PASSWORD=(By.CSS_SELECTOR,'#id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD=(By.CSS_SELECTOR,'#id_registration-password2')
    REGISTER_BUTTON=(By.CSS_SELECTOR,'[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME=(By.CSS_SELECTOR,'div.col-sm-6.product_main > h1')
    SUCCESSFULL_MESSAGE=(By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong')
    PRODUCT_PRICE=(By.CSS_SELECTOR,'p.price_color')
    BASKET_PRICE_MESSAGE=(By.CSS_SELECTOR,'.alert> div > p:nth-child(1) > strong')

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE=(By.CSS_SELECTOR,"#content_inner>p")
    PROCEED_TO_CHECKOUT_BUTTON=(By.CSS_SELECTOR,'.btn.btn-lg')
    BASKET_ITEMS=(By.CSS_SELECTOR,'.basket-items')
