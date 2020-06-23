from page_objects.base_page import BasePage
from page_objects.locators import Locators


class LoginPage(BasePage):

    def insert_username(self, username):
        self.input(Locators.USERNAME, username)

    def insert_password(self, password):
        self.input(Locators.PASSWORD, password)

    def click_submit(self):
        self.single_click(Locators.SUBMIT)

    def login_complete(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_submit()




