from selenium.webdriver.common.by import By


class CommonLocators:
    login_name_field = By.XPATH, "//*[@name='username']"
    login_passwd_fld = By.XPATH, "//*[@name='password']"
    login_button_submit = By.XPATH, "//*[@type='submit']"
    chart_sales_montly = By.XPATH, "//*[@id=chart-sales-monthly']"
    sidebar_menu_main_items = By.XPATH, "//*[@id='box-apps-menu']/li/a"
    sidebar_menu_sub_items = By.XPATH, "//*[@class='selected']/ul//a"
    sticker_line_for_img = By.XPATH, ".//*[contains(@class,'sticker')]"
    img_on_main_page = By.XPATH, "//li/a[@class='link']"
