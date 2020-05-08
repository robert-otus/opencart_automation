def test_opencart_title1(chrome_browser):
    chrome_browser.get('http://localhost/')
    assert chrome_browser.title == 'Your Store'


def test_opencart_title2(firefox_browser):
    firefox_browser.get('http://localhost/')
    assert firefox_browser.title == 'Your Store'


def test_opencart_title3(safari_browser):
    safari_browser.get('http://localhost/')
    assert safari_browser.title == 'Your Store'