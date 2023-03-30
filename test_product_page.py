import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.need_review
@pytest.mark.nine_offers
@pytest.mark.parametrize('query_p', ["/?promo=offer1",
                                     "/?promo=offer2",
                                     "/?promo=offer3",
                                     "/?promo=offer4",
                                     "/?promo=offer5",
                                     "/?promo=offer6",
                                     pytest.param("/?promo=offer7", marks=pytest.mark.xfail\
                                     (reason="The name of the product in the notification is incorrect; test is expected to fail")),
                                     "/?promo=offer8",
                                     "/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, query_p):
    product_page = ProductPage(browser, PRODUCT_URL + query_p)
    product_page.open()
    product_page.should_be_able_to_add_product_to_basket()

@pytest.mark.xfail(reason="success notification should appear; test is expected to fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.click_add_button()
    product_page.should_not_be_success_notification()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.should_not_be_success_notification()

@pytest.mark.xfail(reason="success notification should not disappear; test is expected to fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.click_add_button()
    product_page.success_notification_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
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
        login_page = LoginPage(browser, LOGIN_URL)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        yield
        print("\nPossible teardown steps...")

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, PRODUCT_URL + "/?promo=offer1")
        product_page.open()
        product_page.should_not_be_success_notification()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_URL + "/?promo=offer1")
        product_page.open()
        product_page.should_be_able_to_add_product_to_basket()