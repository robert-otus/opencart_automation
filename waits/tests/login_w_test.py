from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from time import sleep


def test_w_login(chrome_browser):
    chrome_browser.get('http://localhost/')
    wait = WebDriverWait(chrome_browser, 5)
    ac = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.caret')))
    ac.click()
    l = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="https://localhost/index.php?route=account/login"]')))
    l.click()
    #sleep(3)
    assert "Returning Customer"
