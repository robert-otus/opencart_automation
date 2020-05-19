from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(chrome_browser):
    chrome_browser.get("http://localhost/admin/")
    wait = WebDriverWait(chrome_browser, 5)
    un = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    un.send_keys("user")
    p = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    p.send_keys("bitnami1")
    s = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
    s.click()
    lo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.hidden-xs.hidden-sm.hidden-md')))
    lo.click()
    assert "Please enter your login details."



