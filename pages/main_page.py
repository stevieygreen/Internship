from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    TERMS_BTN = (By.XPATH, "//a[@href='/policies/terms-of-service' and contains(@class,'list-menu__item--link')]")
    REFUND_BTN = (By.CSS_SELECTOR, "a[href*='/policies/refund-policy']")
    PRIVACY_BTN = (By.CSS_SELECTOR, "a[href*='/policies/privacy-policy']")
    SHIPPING_BTN = (By.CSS_SELECTOR, "a[href*='/policies/shipping-policy']")
    POP_UP_BTN = (By.XPATH, "//button[@class='popup-close']")
    POLICIES = (By.XPATH, "//h2[contains(text(), 'Our policies')]")

    def open_cureskin(self):
        self.open_url('https://shop.cureskin.com/')
        self.wait_for_element_click(*self.POP_UP_BTN)

    def click_footer_terms(self):
        element = self.wait_for_element_appear(*self.POLICIES)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_element_click(*self.TERMS_BTN)

    def click_footer_refund(self):
        element = self.wait_for_element_appear(*self.REFUND_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_footer_privacy(self):
        element = self.wait_for_element_appear(*self.PRIVACY_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_footer_shipping(self):
        element = self.wait_for_element_appear(*self.SHIPPING_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
