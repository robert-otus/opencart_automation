import pytest
from selenium import webdriver



@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('start-fullscreen')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def safari_browser():
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()




