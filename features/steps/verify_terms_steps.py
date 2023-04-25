from selenium.webdriver.common.by import By
from behave import given, when, then


# Open website
@given('Open Cureskin main page')
def open_amazon(context):
    context.driver.get('https://shop.cureskin.com/')


@when('Click Terms of Service')
def click_search(context):
    context.driver.find_element(By.XPATH, "//a[@href='/policies/terms-of-service' and contains(@class,'list-menu__item--link')]").click()


@then('Verify terms {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.shopify-policy__title").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
