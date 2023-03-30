from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")
    NOTIFICATION = (By.CSS_SELECTOR, "div.alert")
    SUCCESS_NOTIF = (By.CSS_SELECTOR,".alert-success")
    INFO_NOTIF = (By.CSS_SELECTOR, ".alert-info")
    WARNING_NOTIF = (By.CSS_SELECTOR, ".alert-warning")

class BasketPageLocators():
    BASKET_TITLE = (By.CSS_SELECTOR,".basket-title")
    BASKET_SUMMARY = (By.CSS_SELECTOR,".basket_summary")
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")    
    NOTIF_PRODUCT_NAME = (By.CSS_SELECTOR,".alert-success:nth-child(1) strong")
    NOTIF_PRODUCT_PRICE = (By.CSS_SELECTOR,".alert-info strong")