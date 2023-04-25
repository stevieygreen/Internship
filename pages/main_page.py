from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    TERMS_BTN = (By.XPATH, "//a[@href='/policies/terms-of-service' and contains(@class,'list-menu__item--link')]")

    def open_cureskin(self):
        self.open_url('https://shop.cureskin.com/')

    def click_terms(self):
        self.find_element(*self.TERMS_BTN).click()
