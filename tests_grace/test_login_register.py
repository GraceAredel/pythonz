import pytest
from selenium import webdriver

from tests_grace.locators.LoginPageLocators import *
from tests_grace.page_objects.login_register_page import LoginRegisterPage


@pytest.fixture(scope="function")
def log_reg_page(request, driver):
    driver.get(request.config.getoption("--address"))
    return LogRegPage(driver)


@pytest.mark.usefixtures("log_reg_page")
class TestLogin:
    def test_empty_fields_login(self):
        log_reg_page.click_login_button()
        # assert you didnt log in


    def test_correct_name_incorrect_password(self):
        log_reg_page.fill_username_email_field(name_email="username")
        log_reg_page.fill_log_password_field(password="1234")

    def test_login_correct_data(self):

class TestRegister:
    def test_empty_fields_register(self):


    def test_register(self):
