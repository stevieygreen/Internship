from pages.main_page import MainPage
from pages.terms_page import TermsPage
from pages.header_page import HeaderPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.terms_page = TermsPage(self.driver)
        self.header_page = HeaderPage(self.driver)