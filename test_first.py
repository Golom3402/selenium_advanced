import pytest
import os
from selenium import webdriver
from selenium.webdriver.support import wait

from helpers.page_helpers import AuthPage

@pytest.fixture
def driver(request):
    driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    request.addfinalizer(driver.quit)
    return driver

def test_simple(driver):
    driver.get('http://www.google.com/')

def test_login_positive(driver):
    auth_page = AuthPage(driver)
    auth_page.open_admin_page()
    auth_page.login_as()
    assert 'http://localhost/litecart/admin/' == driver.current_url, "После успешного логина браузер перешел на url" \
           f"{driver.current_url}, a должен был перейти на url http://localhost/litecart/admin/"
    wait.WebDriverWait(driver, 5)
    chart_element = driver.find_element_by_xpath('//*[@id="chart-sales-monthly"]')
    assert chart_element
