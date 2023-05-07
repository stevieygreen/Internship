# import allure
# from allure_commons.types import AttachmentType
from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from support.logger import logger, MyListener


# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature
# behave -f allure_behave.formatter:AllureFormatter -o features/ tests


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # ########### CHROME ################
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    # ###################################

    ########### FIREFOX ################
    # options = FirefoxOptions()
    # options.headless = True
    # options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" #for allure
    # context.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
    ###################################

    # ########## BROWSERSTACK ################
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'stevejeanbaptist_mO9S8a'
    # bs_key = 'BgysFFkazpXjr4iAN4aC'
    #
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "10",
    #         "browserVersion": "latest",
    #         "local": "false",
    #         "seleniumVersion": "3.14.0",
    #     },
    #     "browserName": "Chrome",
    # }
    #
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # #########################################

    # ########## Mobile-Web Emulator ################
    #
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)
    # #########################################




    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
