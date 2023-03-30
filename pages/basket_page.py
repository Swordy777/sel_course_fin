from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support.wait import WebDriverWait

class BasketPage(BasePage):
    def basket_present_complex(self): # Takes too long but is more reliable
        self.should_be_basket_title()
        self.should_be_basket_summary()
        self.should_be_basket_items()

    def basket_not_present_complex(self): # Takes too long but is more reliable
        self.should_not_be_basket_title()
        self.should_not_be_basket_summary()
        self.should_not_be_basket_items()

    def should_be_basket_title(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TITLE), "Expected basket to have title"

    def should_be_basket_summary(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_SUMMARY), "Expected basket to have summary"

    def should_be_basket_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Expected basket to contain items"

    def should_not_be_basket_title(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), "Expected basket title to not appear"

    def should_not_be_basket_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Expected basket summary to not appear"

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Expected basket items to not appear"

    git