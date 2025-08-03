from selenium.webdriver.common.by import  By
from pages.base_page import BasePage
from pages.locators import Locators

class LoginPage(BasePage):
    def clear_email(self):
        """Clears the email field"""
        self.clear(Locators.EMAIL_FIELD)

    def fill_email(self, email):
        self.clear(Locators.EMAIL_FIELD)
        self.type(Locators.EMAIL_FIELD, email)

    def fill_password(self, password):
        self.clear(Locators.PASSWORD_FIELD)
        self.type(Locators.PASSWORD_FIELD, password)

    def submit_login(self):
        self.click(Locators.LOGIN_BUTTON)

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()