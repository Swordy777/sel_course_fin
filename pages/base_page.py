import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout = 4): # You can change the timeout if your want
        self.browser = browser
        self.url = url
        self.timeout = timeout
        #self.browser.implicitly_wait(timeout) # not using implicit waits, only explicit, see below
    
    def go_to_basket(self):
        self.should_be_basket_button()
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def go_to_login_page(self):
        self.should_be_login_link()
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"
    
    def should_be_basket_button(self):
        assert self.browser.find_element(*BasePageLocators.BASKET_BUTTON), "Can't find 'add to basket' button"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")