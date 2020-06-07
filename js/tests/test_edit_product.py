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
    ch = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.fa.fa-pencil')))
    actions_click(chrome_browser, ch[15])
    sleep(3)
    dt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="#tab-data"]')))
    actions_click(chrome_browser, dt)
    md = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-price')))
    actions_d_click(chrome_browser, md, '99')
    sleep(3)
    sv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.pull-right button')))
    actions_click(chrome_browser, sv)
    sleep(9)


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


def actions_d_click(driver, element, key):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.double_click()
    actions.send_keys(key)
    return actions.perform()




