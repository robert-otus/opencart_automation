from selenium.webdriver.common.by import By


class Locators:
    USERNAME = (By.CSS_SELECTOR, '#input-username')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    SUBMIT = (By.CSS_SELECTOR, '.btn.btn-primary')
    CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    PRODUCT = (By.CSS_SELECTOR, '.collapse.in li')
    ADD = (By.CSS_SELECTOR, '.fa.fa-plus')
    P_NAME = (By.CSS_SELECTOR, '#input-name1.form-control')
    M_TAG = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA = (By.CSS_SELECTOR, '[href="#tab-data"]')
    MODEL = (By.CSS_SELECTOR, '#input-model')
    SAVE = (By.CSS_SELECTOR, '.fa.fa-save')
    SAVE1 = (By.CSS_SELECTOR, '.pull-right')
    EDIT = (By.CSS_SELECTOR, '.fa.fa-pencil')
    PRICE = (By.CSS_SELECTOR, '#input-price')
    CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    DEL = (By.CSS_SELECTOR, '.fa.fa-trash-o')
    FILTER_PN = (By.CSS_SELECTOR, '[name="filter_name"]')
    FILTER_BUT = (By.CSS_SELECTOR, '#button-filter')
    COPY = (By.CSS_SELECTOR, '.fa.fa-copy')
    MOD = (By.CSS_SELECTOR, '.fa.fa-check-circle')
    SALES = (By.CSS_SELECTOR, '#menu-sale')
    ORDERS = (By.CSS_SELECTOR, '.collapse.in li a')
    REPORTS_MENU = (By.CSS_SELECTOR, '#menu-report')
    REPORTS = (By.CSS_SELECTOR, '.collapse.in li a')




