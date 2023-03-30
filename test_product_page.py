import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage

@pytest.mark.nine_offers
@pytest.mark.parametrize('query_p', ["?promo=offer1",
                                    "?promo=offer2",
                                    "?promo=offer3",
                                    "?promo=offer4",
                                    "?promo=offer5",
                                    "?promo=offer6",
                                    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                    "?promo=offer8",
                                    "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, query_p):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link + query_p)
    product_page.open()
    product_page.should_be_able_to_add_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_button()
    assert product_page.is_not_element_present(*BasePageLocators.SUCCESS_NOTIF), "Success notification appeared after adding to basket; expected it to not appear"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*BasePageLocators.SUCCESS_NOTIF), "Success notification appeared on product page; expected it to not appear"

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_button()
    assert product_page.is_disappeared(*BasePageLocators.SUCCESS_NOTIF), "Expected notification to disappear, but it stayed"

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fake.mail.com"
        print(email)
        password = "1qaz@WSX#EDC"
        login_page = LoginPage(browser, "https://selenium1py.pythonanywhere.com/ru/accounts/login/")
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        yield
        print("\nPossible teardown steps...")

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer1"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_not_element_present(*BasePageLocators.SUCCESS_NOTIF), "Success notification appeared on product page; expected it to not appear"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_able_to_add_product_to_basket()