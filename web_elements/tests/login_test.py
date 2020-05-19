def test_login(chrome_browser):
    chrome_browser.get('http://localhost/')
    ac = chrome_browser.find_element_by_css_selector('.caret')
    ac.click()
    l = chrome_browser.find_element_by_css_selector('[href="https://localhost/index.php?route=account/login"]')
    l.click()
    assert "Returning Customer"
