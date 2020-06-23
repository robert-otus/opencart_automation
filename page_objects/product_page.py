from page_objects.base_page import BasePage
from page_objects.locators import Locators
from time import sleep


class ProductPage(BasePage):
    def add_product(self, name, tag, model):
        self.single_click(Locators.ADD)
        self.input(Locators.P_NAME, name)
        self.input(Locators.M_TAG, tag)
        self.single_click(Locators.DATA)
        self.input(Locators.MODEL, model)
        self.single_click(Locators.SAVE)

    def edit_product(self, price):
        e = self.find_elements(Locators.EDIT)
        e[13].click()
        self.single_click(Locators.DATA)
        sleep(3)
        self.clear(Locators.PRICE)
        sleep(3)
        self.input(Locators.PRICE, price)
        self.single_click(Locators.SAVE)

    def delete_product(self):
        ch = self.find_elements(Locators.CHECKBOX)
        ch[14].click()
        self.single_click(Locators.DEL)
        self.alert()
        sleep(3)

    def filter(self, prod):
        self.input(Locators.FILTER_PN, prod)
        self.single_click(Locators.FILTER_BUT)

    def copy_product(self):
        ch = self.find_elements(Locators.CHECKBOX)
        ch[1].click()
        self.single_click(Locators.COPY)
        sleep(3)









