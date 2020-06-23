import pytest
from selenium import webdriver
from page_objects.application import Application



@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('start-fullscreen')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    #driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def safari_browser():
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def app(chrome_browser):
    page = Application(chrome_browser)
    page.login.go_to()
    return page


# @pytest.fixture()
# def app(request):
#     # Before
#     options = webdriver.ChromeOptions()
#     options.add_argument('start-fullscreen')
#     options.add_argument('--ignore-certificate-errors')
#     # options.add_argument("headless")
#     driver = webdriver.Chrome(options=options)
#     fixture = Application(driver)
#
#     # After
#
#     def fin():
#         driver.quit()
#     request.addfinalizer(fin)
#
#     return fixture






