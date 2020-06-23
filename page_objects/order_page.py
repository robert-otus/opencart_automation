from page_objects.base_page import BasePage
from page_objects.locators import Locators


class OrderPage(BasePage):
    def check_orders(self):
        self.single_click(Locators.SALES)
        o = self.find_elements(Locators.ORDERS)
        o[0].click()
