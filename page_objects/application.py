from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.order_page import OrderPage
from page_objects.report_page import ReportPage
# from page_objects.base_page import BasePage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.login = LoginPage(self)
        self.main = MainPage(self)
        self.product = ProductPage(self)
        self.order = OrderPage(self)
        self.report = ReportPage(self)
        # self.base = BasePage(self)


