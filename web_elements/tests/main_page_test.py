def test_main_paige(chrome_browser):
    chrome_browser.get('http://localhost/')
    cu = chrome_browser.find_element_by_css_selector('.list-unstyled [href = "http://localhost/index.php?route=information/contact"]')
    cu.click()
    assert "Our Location"


