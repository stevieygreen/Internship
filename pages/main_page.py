from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    TERMS_BTN = (By.XPATH, "//a[@href='/policies/terms-of-service' and contains(@class,'list-menu__item--link')]")
    REFUND_BTN = (By.CSS_SELECTOR, "a[href*='/policies/refund-policy']")
    PRIVACY_BTN = (By.CSS_SELECTOR, "a[href*='/policies/privacy-policy']")
    SHIPPING_BTN = (By.CSS_SELECTOR, "a[href*='/policies/shipping-policy']")

    def open_cureskin(self):
        self.open_url('https://shop.cureskin.com/')

    def click_footer_terms(self):
        self.find_element(*self.TERMS_BTN).click()

    def click_footer_refund(self):
        self.find_element(*self.REFUND_BTN).click()

    def click_footer_privacy(self):
        self.find_element(*self.PRIVACY_BTN).click()

    def click_footer_shipping(self):
        self.find_element(*self.SHIPPING_BTN).click()
