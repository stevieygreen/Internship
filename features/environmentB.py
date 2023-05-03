from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    service = Service('C:/Users/steve/OneDrive/Desktop/Internship_Folder/Internship/chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)

    # service = Service('C:/Users/steve/OneDrive/Desktop/Internship_Folder/Internship/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)



    # context.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox(executable_path="geckodriver.exe")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
