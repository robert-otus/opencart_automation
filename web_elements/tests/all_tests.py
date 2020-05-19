def test_all_main_page(chrome_browser):
    open_main_page(chrome_browser)
    single_click(chrome_browser, '.list-unstyled [href = "http://localhost/index.php?route=information/contact"]')
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
    i = find_elements_css(chrome_browser, '.collapse.in li')
    i[1].click()
    assert "Product List"


def open_admin_page(driver):
    driver.get("http://localhost/admin/")


def open_main_page(driver):
    driver.get("http://localhost/")


def find_element_css(driver, csslocator):
    return driver.find_element_by_css_selector(csslocator)


def find_elements_css(driver, csslocator):
    return driver.find_elements_by_css_selector(csslocator)


def single_click(driver, csslocator):
    s = find_element_css(driver, csslocator)
    s.click()


def type_text(driver, csslocator, value):
    e = find_element_css(driver, csslocator)
    e.send_keys(value)


def enter_user_name(driver, email):
    type_text(driver, '#input-username', email)


def enter_password(driver, password):
    type_text(driver, '#input-password', password)





























