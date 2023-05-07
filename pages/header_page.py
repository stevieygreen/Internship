from selenium.webdriver.common.by import By
from pages.base_page import Page


class HeaderPage(Page):
    HOME_BTN = (By.CSS_SELECTOR, "a.header__heading-link.focus-inset")
    POLICIES = (By.XPATH, "//h2[contains(text(), 'Our policies')]")

    def click_home_btn(self):
        self.find_element(*self.HOME_BTN).click()

