from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_main_page(chrome_browser):
    open_main_page(chrome_browser)
    single_click(chrome_browser, '.list-unstyled '
                                 '[href = "http://localhost/index.php?route=information/contact"]')
    assert "Our Location"
    single_click(chrome_browser, '.caret')
    single_click(chrome_browser, '[href="https://localhost/index.php?route=account/login"]')
    assert "Returning Customer"


def test_all_admin(chrome_browser):
    open_admin_page(chrome_browser)
    enter_user_name(chrome_browser, 'user')
    enter_password(chrome_browser, 'bitnami1')
    single_click(chrome_browser, '.btn.btn-primary')
    assert chrome_browser.title == 'Dashboard'
    single_click(chrome_browser, '#menu-catalog')
    i = elements_presence(chrome_browser, '.collapse.in li')
    i[1].click()
    e = elements_presence(chrome_browser, '.fa.fa-pencil')
    e[0].click()
    assert "Product List"
    single_click(chrome_browser, '.hidden-xs.hidden-sm.hidden-md')


def open_admin_page(driver):
    driver.get("http://localhost/admin/")


def open_main_page(driver):
    driver.get("http://localhost/")


def element_visibility_css(driver, csslocator):
    wait = WebDriverWait(driver, 5)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, csslocator)))


def element_clickable_css(driver, csslocator):
    wait = WebDriverWait(driver, 5)
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, csslocator)))


def elements_presence(driver, csslocator):
    wait = WebDriverWait(driver, 5)
    return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, csslocator)))


def single_click(driver, csslocator):
    s = element_clickable_css(driver, csslocator)
    s.click()


def type_text(driver, csslocator, value):
    e = element_visibility_css(driver, csslocator)
    e.send_keys(value)


def enter_user_name(driver, email):
    type_text(driver, '#input-username', email)


def enter_password(driver, password):
    type_text(driver, '#input-password', password)
