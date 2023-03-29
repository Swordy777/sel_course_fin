import re
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_able_to_add_product_to_basket(self):
        self.should_be_product_name()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        self.should_be_product_price()
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = self.digitize_price(product_price.text)

        self.should_be_add_button()
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()

        notifs = self.should_have_notifications()
        self.is_notif_product_name_correct(product_name)
        self.is_notif_basket_price_correct(product_price)


        
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Can't find product name"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Can't find product price"

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Can't find add button"

    def should_have_notifications(self):
        notifs = self.browser.find_elements(*ProductPageLocators.NOTIFICATION)
        assert len(notifs) != 0, "No notifications about adding product to basket found"
        return notifs

    def is_notif_product_name_correct(self, pname):
        notif_pname = self.browser.find_element(*ProductPageLocators.NOTIF_PRODUCT_NAME).text
        assert notif_pname == pname, f"Product name on product page - '{pname}' and product name in the notification differ - '{notif_pname}', expected to match"

    def is_notif_basket_price_correct(self, pprice):
        notif_pprice = self.browser.find_element(*ProductPageLocators.NOTIF_PRODUCT_PRICE)
        notif_pprice = self.digitize_price(notif_pprice.text)
        assert notif_pprice == pprice, f"Basket total cost in notification - '{notif_pprice}' differs from product price - '{pprice}', expected to match"
    
    def digitize_price(self, input):
        input = re.match(r"\D*(\d*[,.]\d*)\D*",input).group(1).replace(",",".")
        input = float(input)
        return input
        
