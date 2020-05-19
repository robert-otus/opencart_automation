from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_paige_w(chrome_browser):
    chrome_browser.get('http://localhost/')
    wait = WebDriverWait(chrome_browser, 5)
    cu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.list-unstyled '
                                                '[href = "http://localhost/index.php?route=information/contact"]')))
    cu.click()
    assert "Our Location"