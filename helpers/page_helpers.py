from locators import CommonLocators as lctrs

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