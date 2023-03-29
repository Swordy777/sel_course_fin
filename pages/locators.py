from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    NOTIFICATION = (By.CSS_SELECTOR, "div.alertinner")
    NOTIF_PRODUCT_NAME = (By.XPATH,"//div[contains(@class,'alert')][1]/div[@class='alertinner ']/strong")
    NOTIF_PRODUCT_PRICE = (By.XPATH,"//div[contains(@class,'alert')][3]/div[@class='alertinner ']/p/strong")