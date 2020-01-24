from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from tests_grace.locators.LoginPageLocators import *


class LoginRegisterPage:
    """base class for methods on /login page"""

    def __init__(self, driver):
        self.driver = driver

    def _get_element(self, *locator):
        return self.driver.find_element(*locator)

    def _get_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def _wait_element(self, by, value, delay=10):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            return False


    def fill_username_email_field(self, name_email):
        els = self.driver.find_elements(*LoginPageFieldLocators.USERNAME_OR_EMAIL)
        field = els[0]
        field.send_keys(name_email)

    def fill_log_password_field(self, password):
        els = self.driver.find_elements(*LoginPageFieldLocators.PASSWORD)
        field = els[0]
        field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageFieldLocators.LOGIN_BUTTON).click()

    def login(self, name_email, password):
        self.fill_username_email_field(name_email)
        self.fill_log_password_field(password)
        self.click_login_button()

    def fill_username_field(self, name):
        els = self.driver.find_elements(*RegisterFieldLocators.USERNAME)
        field = els[1]
        field.send_keys(name)

    def fill_email_field(self, email):
        els = self.driver.find_elements(*RegisterFieldLocators.EMAIL)
        field = els[1]
        field.send_keys(email)

    def fill_reg_password_field(self, password):
        els = self.driver.find_elements(*RegisterFieldLocators.PASSWORD)
        field = els[1]
        field.send_keys(password)

    def click_signin_button(self):
        self.driver.find_element(*RegisterFieldLocators.REGISTER_BUTTON).click()

    def register(self, name, email, password):
        self.fill_username_field(name)
        self.fill_email_field(email)
        self.fill_reg_password_field(password)
        self.click_signin_button()
