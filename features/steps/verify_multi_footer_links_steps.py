from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Verify {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.terms_page.verify_terms_page(expected_result)

#def verify_search_result(context, expected_result):
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.shopify-policy__title").text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

@when ('Go back to home page')
def back_to_home(context):
    context.app.header_page.click_home_btn()


@when ('Click "Refund policy"')
def click_refund(context):
    context.app.main_page.click_footer_refund()


@when ('Click "Privacy Policy"')
def click_privacy(context):
    context.app.main_page.click_footer_privacy()


@when ('Click "Shipping Policy"')
def click_privacy(context):
    context.app.main_page.click_footer_shipping()