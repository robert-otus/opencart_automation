from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_order_check_w(chrome_browser):
    chrome_browser.get('http://localhost/admin/')
    wait = WebDriverWait(chrome_browser, 5)
    l = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    l.send_keys("user")
    p = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    p.send_keys("bitnami1")
    s = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
    s.click()
    tf = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.tile-footer')))
    tf[0].click()
    assert "Order List"