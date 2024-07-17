# features/steps/steps.py
import time
from behave import given, when
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('the user navigates to')
def step_given_user_navigates_to_url(context, url):
    #context.browser = webdriver.Chrome()  # or any other browser driver
    chrome_driver_path = 'C:/Users/gaddadak/OneDrive - CDK Global LLC/Documents/BDD_Python/drivers/chromedriver.exe'
    service = service(chrome_driver_path)
    context = webdriver.Chrome(service=service)
    context.maximize_window()
    context.browser.get("https://service-app.connectcdk.com/?cid=269")


@when('the user enters the username')
def step_when_user_enters_username(context, username):
    username_field = context.browser.find_element(By.XPATH,("//input[@id='ctl00_ctl00_Main_Main_txtUsernameSF']"))  # Update the locator as per your page
    username_field.send_keys('adp_csr')

@when('the user enters the password')
def step_when_user_enters_password(context, password):
    password_field = context.browser.find_element(By.XPATH,("//*[@id='ctl00_ctl00_Main_Main_txtPasswordSF']"))  # Update the locator as per your page
    password_field.send_keys('lUZNqVCu%b')
    time.sleep(10)

@when('the user clicks the login button')
def step_when_user_clicks_login_button(context):
    login_button = context.browser.find_element(By.XPATH,('/html/body/form/div[8]/div[2]/div[2]/div[1]/div/div[6]/input'))  # Update the locator as per your page
    login_button.click()
    time.sleep(10)



# Closing the browser after each scenario
def after_scenario(context, scenario):
    context.browser.quit()
