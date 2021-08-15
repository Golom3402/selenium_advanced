import os

from selenium import webdriver
from helpers.page_helpers import AuthPage, AdminPage


class Application:
    def __init__(self, browser):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chromedriver")

            self.driver = webdriver.Chrome(executable_path=driver_path)

        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.driver.set_window_size(1920, 1080)

        self.admin = AdminPage(self.driver)
        self.auth = AuthPage(self.driver)