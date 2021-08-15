from selenium.webdriver.common.by import By


class CommonLocators:
    login_name_field = By.XPATH, "//*[@name='username']"
    login_passwd_fld = By.XPATH, "//*[@name='password']"
    login_button_submit = By.XPATH, "//*[@type='submit']"
    chart_sales_montly = By.XPATH, "//*[@id=chart-sales-monthly']"
