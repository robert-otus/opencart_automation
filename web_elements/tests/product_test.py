def test_product(chrome_browser):
    chrome_browser.get('http://localhost/admin/')
    l = chrome_browser.find_element_by_css_selector('#input-username')
    l.send_keys("user")
    p = chrome_browser.find_element_by_css_selector('#input-password')
    p.send_keys("bitnami1")
    s = chrome_browser.find_element_by_css_selector('.btn.btn-primary')
    s.click()
    ct = chrome_browser.find_element_by_css_selector('#menu-catalog')
    ct.click()
    pr = chrome_browser.find_elements_by_css_selector('.collapse.in li')
    pr[1].click()
    e = chrome_browser.find_elements_by_css_selector('.fa.fa-pencil')
    e[0].click()
    assert "Edit Product"
