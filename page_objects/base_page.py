from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage(object):

    def __init__(self, app, wait=5):
        self.app = app
        self.base_url = "http://localhost/admin/"
        self.wait = WebDriverWait(self.app.driver, wait)
        #self.actions = ActionChains(driver)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def single_click(self, locator):
       self.find_element(locator).click()

    # def double_click(self, locator, key):
    #     self.actions.move_to_element(locator)
    #     self.actions.double_click()
    #     self.actions.send_keys(key)
    #     return self.actions.perform()

    def clear(self, locator):
        self.find_element(locator).clear()

    def input(self, locator, key):
        self.find_element(locator).send_keys(key)

    def go_to(self):
        return self.app.driver.get(self.base_url)

    def alert(self):
        return self.app.driver.switch_to_alert().accept()
