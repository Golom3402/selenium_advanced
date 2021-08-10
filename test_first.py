import pytest
import os
from selenium import webdriver

@pytest.fixture
def driver(request):
    driver_path = os.path.join(os.path.dirname(__file__),'chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    request.addfinalizer(driver.quit)
    return driver

def test_simple(driver):
    driver.get('http://www.google.com/')

