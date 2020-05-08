import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    #options.add_argument('start-fullscreen')
    driver = webdriver.Chrome(options=options)
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




