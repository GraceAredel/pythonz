import pytest
from selenium import webdriver

from tests_grace.locators.LoginPageLocators import *
from tests_grace.page_objects.login_register_page import LoginRegisterPage


@pytest.fixture(scope="function")
def log_reg_page(request, driver):
    driver.get(request.config.getoption("--address"))
    return LogRegPage(driver)


class TestLogin:
    def test_empty_fields_login(self):


    def test_correct_name_incorrect_password(self):

    def test_login_correct_data(self):



class TestRegister:
    def test_empty_fields_register(self):


    def test_register(self):
