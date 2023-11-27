from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()

email = os.getenv('email')
pw = os.getenv('pw')
num = os.getenv('num')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs")

driver.maximize_window()

login_button = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div'
                                             '/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
time.sleep(2)
login_button.click()

facebook_login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="s2018968691"]/main/div[1]/div/div[1]/div/div/'
                                                'div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div'))).click()

main_window_handle = driver.window_handles[0]
popup_window_handle = driver.window_handles[1]
driver.switch_to.window(popup_window_handle)

try:
    accept_cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@title="Allow all cookies"]')))
    accept_cookies.click()
except Exception as e:
    print(f"An error occurred: {e}")

# Facebook Login Pop Up window
fb_email = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_email.send_keys(f'{email}')
fb_pw = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_pw.send_keys(f'{pw}')
fb_login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]')))
fb_login.click()

driver.switch_to.window(main_window_handle)
try:
    allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[text()="Allow" and @class="l17p5q9z"]')))
    allow_button.click()
except Exception as e:
    print(f"Error:{e}")

not_interested = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')))
not_interested.click()

try:
    maybe_later = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[1]/div/div[3]/button[2]/div[2]/div[2]')))
    maybe_later.click()
except Exception as e:
    print(f"Error: {e}")

cookies_tinder = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, ' //*[@id="s-547617529"]/div/div[2]/div/'
                                               'div/div[1]/div[1]/button/div[2]/div[2]')))
cookies_tinder.click()

try:
    # Continuous key press simulation using ActionChains
    actions = ActionChains(driver)
    while True:
        actions.send_keys(Keys.ARROW_LEFT).perform()
        time.sleep(1)  # Add a delay to control the speed of key presses

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (e.g., press Ctrl+C to stop the loop)
    pass

