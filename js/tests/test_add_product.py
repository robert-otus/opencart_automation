from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep


def test_add_prod(chrome_browser):
    chrome_browser.get('http://localhost/admin/')
    wait = WebDriverWait(chrome_browser, 5)
    l = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    l.send_keys("user")
    p = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    actions_keys(chrome_browser, p, "bitnami1")
    s = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
    s.click()
    ct = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu-catalog')))
    ct.click()
    pr = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.collapse.in li')))
    pr[1].click()
    a = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa.fa-plus')))
    actions_click(chrome_browser, a)
    pn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-name1.form-control')))
    actions_keys(chrome_browser, pn, "Phone 3")
    sleep(2)
    mt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-meta-title1')))
    actions_keys(chrome_browser, mt, "P-3")
    sleep(3)
    # dp = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.note-editable.panel-body')))
    dt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="#tab-data"]')))
    actions_click(chrome_browser, dt)
    md = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-model')))
    actions_keys(chrome_browser, md, 'P-R-3.3')
    sleep(2)
    sv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa.fa-save')))
    actions_click(chrome_browser, sv)
    sleep(6)


def actions_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    return actions.perform()


def actions_keys(driver, element, key):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.send_keys(key)
    return actions.perform()
