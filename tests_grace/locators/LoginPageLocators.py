"""this file contains locators for elements on login page"""
from selenium.webdriver.common.by import By


class LoginPageFieldLocators(object):
    """class for the locators in login field"""
    USERNAME_OR_EMAIL = (By.ID, "id_username")  # 0
    PASSWORD = (By.ID, "id_password")  # 1
    LOGIN_BUTTON = (By.CLASS_NAME, "btn.btn-block.btn-primary")


class RegisterFieldLocators(object):
    """class for the locators in register field"""
    USERNAME = (By.ID, "id_username")  # 0
    EMAIL = (By.ID, "id_email")
    PASSWORD = (By.ID, "id_password")  # 1
    REGISTER_BUTTON = (By.CLASS_NAME, "btn.btn-block.btn-primary")
