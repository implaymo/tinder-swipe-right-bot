from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

load_dotenv()

phone_number = os.getenv('num')

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
                                                'div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')))
facebook_login.click()



decline_cookies = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, '//*[@id="u_0_g_a/"]')))
decline_cookies.click()
# enter_number = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, '//*[@id="s2018968691"]/main/div[1]/div[1]/'
#                                                 'div/div[2]/div/div[2]/div/div[2]/input')))
# enter_number.send_keys(f'{phone_number}')
#
#
# continue_button = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, '//*[@id="s2018968691"]/main/div[1]/'
#                                                 'div[1]/div/div[3]/button/div[2]/div[2]')))
# continue_button.click()
