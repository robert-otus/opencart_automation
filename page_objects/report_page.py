from page_objects.base_page import BasePage
from page_objects.locators import Locators


class ReportPage(BasePage):
    def check_reports(self):
        self.single_click(Locators.REPORTS_MENU)
        self.single_click(Locators.REPORTS)
