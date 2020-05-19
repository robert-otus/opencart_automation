def test_admin_credentials(chrome_browser):
    chrome_browser.get('http://localhost/admin/')
    l = chrome_browser.find_element_by_css_selector('#input-username')
    l.send_keys("user")
    p = chrome_browser.find_element_by_css_selector('#input-password')
    p.send_keys("bitnami1")
    s = chrome_browser.find_element_by_css_selector('.btn.btn-primary')
    s.click()
    assert chrome_browser.title == 'Dashboard'
