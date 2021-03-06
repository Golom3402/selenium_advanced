from locators import CommonLocators as lctrs
from lxml import html, etree


class AuthPage:

    def __init__(self, driver):
        self.driver = driver

    def open_admin_page(self):
        self.driver.get(url='http://localhost/litecart/admin/')

    def login_as(self, name=None, passwd=None):
        login_field = self.driver.find_element(*lctrs.login_name_field)
        login_field.click()
        login_field.clear()
        login_field.send_keys(f'{name}' if name else 'admin')
        passwd_field = self.driver.find_element(*lctrs.login_passwd_fld)
        passwd_field.click()
        passwd_field.clear()
        passwd_field.send_keys(f'{passwd}' if passwd else 'admin')
        submit_btn = self.driver.find_element(*lctrs.login_button_submit)
        submit_btn.click()

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def get_all_sidebar_menu_item_elements(self):
        elements = self.driver.find_elements(*lctrs.sidebar_menu_main_items)
        return elements

    def get_all_sidebar_menu_sub_elements(self):
        sub_elements = self.driver.find_elements(*lctrs.sidebar_menu_sub_items)
        return sub_elements

class CountryPage:

    def __init__(self, driver):
        self.driver = driver

    def read_all_country_on_page(self, page="common"):
        if page == "common":
            name_locator = lctrs.country_page_country_name
        else:
            name_locator = lctrs.country_name_on_edit_country_page
        element_list = self.driver.find_elements(*name_locator)
        names_list = []
        for i in element_list:
            names_list.append(i.text)
        return names_list

def check_sort(test_list):
    ref_list = sorted(test_list.copy())
    return ref_list == test_list

