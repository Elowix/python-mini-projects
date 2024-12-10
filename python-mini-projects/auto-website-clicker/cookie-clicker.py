import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "./chromedriver-linux64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://orteil.dashnet.org/cookieclicker/')

lang_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
)
lang_button.click()

big_cookie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'bigCookie'))
)

for _ in range(100):
    big_cookie.click()

time.sleep(2)  
