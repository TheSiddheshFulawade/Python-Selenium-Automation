import os
import time
import pyperclip


from pyrobot import Robot
robot=Robot()
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains

keyboard = Controller()

app_array = ['MUM006616','MUM008426','MUM007813','MUM005188','MUM007196']

os.environ['PATH'] += r"C:\Users\swara\Downloads\chromedriver_win32"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://board.sgbregistration.in/")
time.sleep(20)
actions = ActionChains(driver)

# Find the APPLICATION LIST option and click on it
dropdown = driver.find_element(By.XPATH, '//div[@class="dropdown"]/button')
dropdown.click()
time.sleep(2)

app_list_option = driver.find_element(By.XPATH, '//div[@class="dropdown-content"]/a[text()="Application List"]')
app_list_option.click()
time.sleep(2)

for a in app_array:
    # Searching for the Application Number
    app_number = driver.find_element(By.XPATH, '//input[@id ="ipAppNum"][@type="text"]')
    app_number.click()
    app_number.clear()
    app_number.send_keys(a)
    pyperclip.copy(a)

    time.sleep(2)

    search_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    search_button.click()
    time.sleep(2)

    # Viewing the entered Application Number
    view_button = driver.find_element(By.XPATH, '//button[@title="View Details"]')
    view_button.click()
    time.sleep(2)

    # Print Application
    print_application = driver.find_element(By.XPATH, '//button[@class="btn hide-print mt-3 ml-2 float-right btn-info btn-sm"]')
    print_application.click()
    time.sleep(7)

    # Print B-Form Receipt
    print_Bform_receipt = driver.find_element(By.XPATH, '//button[@class="btn hide-print mt-3 ml-2 float-right btn-success btn-sm"]')
    print_Bform_receipt.click()
    time.sleep(5)
    b = str(a)+' B-Form Receipt'
    pyperclip.copy(b)

    print_Bform_preview_receipt = driver.find_element(By.XPATH, '//button[@class="btn float-right mt-2 btn-info"]')
    print_Bform_preview_receipt.click()
    time.sleep(5)

    print_Bform_preview_receipt = driver.find_element(By.XPATH, '//button[@class="close"]')
    print_Bform_preview_receipt.click()
    time.sleep(12)

    #Back to Home
    back_button = driver.find_element(By.XPATH, '//button[@class="btn hide-print mt-3 ml-2 float-right btn-secondary btn-sm"]')
    back_button.click()
    time.sleep(2)


print("Done")



