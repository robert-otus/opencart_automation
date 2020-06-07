from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep


def test_admin_credentials(chrome_browser):
    chrome_browser.get('http://localhost/admin/')
    wait = WebDriverWait(chrome_browser, 5)
    l = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    actions = ActionChains(chrome_browser)
    actions.move_to_element(l)
    actions.click(l)
    actions.send_keys("user")
    actions.perform()
    sleep(3)
    #l.send_keys("user")
    p = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    p.send_keys("bitnami1")
    s = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
    s.click()
    assert chrome_browser.title == 'Dashboard'