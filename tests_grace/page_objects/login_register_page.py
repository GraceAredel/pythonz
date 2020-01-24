from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


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


    def fill_log_password_field(self):


    def click_login_button(self):


    def login(self):
        self.fill_username_email_field()
        self.fill_log_password_field()
        self.click_login_button()


    def fill_username_field(self, name):


    def fill_email_field(self, email):


    def fill_reg_password_field(self, password):


    def click_signin_button(self):


    def register(self):
        self.fill_username_field(name)
        self.fill_email_field(email)
        self.fill_reg_password_field(password)
        self.click_signin_button()
