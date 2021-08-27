import pytest
from selenium.webdriver.support import wait
from helpers.app import Application
from helpers.page_helpers import check_sort
from locators import CommonLocators as lctrs


@pytest.fixture
def app(request):
    app = Application(browser='chrome')

    wait.WebDriverWait(app.driver, 5)
    request.addfinalizer(app.driver.quit)
    return app

def test_simple(app):
    app.driver.get('http://www.google.com/')

def test_login_positive(app):
    app.auth.open_admin_page()
    app.auth.login_as()
    assert 'http://localhost/litecart/admin/' == app.driver.current_url, "После успешного логина браузер перешел" \
           f" на url {app.driver.current_url}, a должен был перейти на url http://localhost/litecart/admin/"
    chart_element = app.driver.find_element_by_xpath('//*[@id="chart-sales-monthly"]')
    assert chart_element


def test_click_to_each_items_in_sidebar(app):
    app.auth.open_admin_page()
    app.auth.login_as()
    admin = app.admin
    common_len = len(admin.get_all_sidebar_menu_item_elements())
    menu_list = {}
    for i in range(common_len):
        main_item_menu_elements = admin.get_all_sidebar_menu_item_elements()
        main_item_menu_elements[i].click()
        sub_elements_len = len(admin.get_all_sidebar_menu_sub_elements())
        menu_list[f'{i}'] = sub_elements_len
        assert app.driver.find_element_by_xpath("//h1")
        for s in range(sub_elements_len):
            sub_elements = admin.get_all_sidebar_menu_sub_elements()
            sub_elements[s].click()
            assert app.driver.find_element_by_xpath("//h1")

def test_for_8_labor(app):
    app.driver.get("http://localhost/litecart/en/")
    common_len_of_images = len(app.driver.find_elements(*lctrs.img_on_main_page))
    for i in range(common_len_of_images):
        test_img = app.driver.find_elements(*lctrs.img_on_main_page)[i]
        label_count = test_img.find_elements(*lctrs.sticker_line_for_img)
        assert len(label_count) == 1, f"В товаре {test_img.get_attribute('title')} на главной странице нашли " \
                                      f"{len(label_count)} стикеров, а ожидали найти 1 стикер"

def test_for_9(app):
    app.driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    app.auth.login_as('admin', 'admin')
    top_level_names = app.country.read_all_country_on_page()
    assert check_sort(top_level_names), "названия стран не отсортированы по имени"
    zones_elements = app.driver.find_elements(*lctrs.country_page_zones_count)
    for i in range(len(zones_elements)):
        elements = app.driver.find_elements(*lctrs.country_page_zones_count)
        current_zones_count = elements[i].text
        if int(current_zones_count) > 0:
            app.driver.find_elements(*lctrs.country_page_country_name)[i].click()
            inner_zones_names = app.country.read_all_country_on_page(page='inner')
            assert check_sort(inner_zones_names), 'названия зон в на странице редактирования страны' \
                                                  ' не отсортированы по имени'
            app.driver.back()
