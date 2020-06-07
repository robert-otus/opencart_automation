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
    ch = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="checkbox"]')))
    actions_click(chrome_browser, ch[16])
    sleep(3)
    d = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa.fa-trash-o')))
    actions_click(chrome_browser, d)
    sleep(3)
    chrome_browser.switch_to_alert().accept()
    sleep(4)


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
