from page_objects.base_page import BasePage
from page_objects.locators import Locators


class MainPage(BasePage):
    def cat_list(self):
        self.single_click(Locators.CATALOG)
        p = self.find_elements(Locators.PRODUCT)
        p[1].click()
