import pytest
from pages.login_page import LoginPage
from utils.singleton_browser import SingletonBrowser
from utils.driver_factory import get_base_url
import os

@pytest.mark.webui
def test_successful_login():
    driver = SingletonBrowser()
    driver.get(get_base_url())
    login_page = LoginPage(driver)
    login_page.login(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))
    assert "admin" in driver.current_url
