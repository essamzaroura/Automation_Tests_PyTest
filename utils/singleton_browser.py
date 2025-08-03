from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SingletonBrowser:
    _instance = None
    # def __new__(cls):
    #     if cls.__instance is None:
    #         options = webdriver.ChromeOptions()
    #         options.add_argument("--headless=new")
    #         options.add_argument("--start-maximized")
    #         cls._instance = webdriver.Chrome(options=options)
    #     return cls._instance

    def __new__(cls):
        if not cls._instance:
            service = Service(ChromeDriverManager().install())
            cls._instance = webdriver.Chrome(service=service)
            cls._instance.maximize_window()
        return cls._instance

    @classmethod
    def quit(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None