from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsPage(Page):
    TERMS_HEADER = (By.CSS_SELECTOR, "div.shopify-policy__title")

    def verify_terms_page(self, expected_text):
        self.verify_text(expected_text, *self.TERMS_HEADER)