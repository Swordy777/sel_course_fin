import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

@pytest.mark.sevenlinks
@pytest.mark.pp_tests
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_able_to_add_product_to_basket()

@pytest.mark.pp_tests
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #TODO: implement the test
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_button()
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_NOTIF), "Success notification appeared after adding to basket; expected it to not appear"

@pytest.mark.pp_tests
def test_guest_cant_see_success_message(browser):
    #TODO: implement the test
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_NOTIF), "Success notification appeared on product page; expected it to not appear"

@pytest.mark.pp_tests
def test_message_disappeared_after_adding_product_to_basket(browser):
    #TODO: implement the test
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_button()
    assert product_page.is_disappeared(*ProductPageLocators.SUCCESS_NOTIF), "Expected notification to disappear, but it stayed"