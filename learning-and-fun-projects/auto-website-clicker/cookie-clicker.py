import time  
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()  
driver.get('https://orteil.dashnet.org/cookieclicker/') 


element = WebDriverWait(driver, 10).until(  
    EC.element_to_be_clickable((By.ID, 'langSelect-EN'))  
)  
element.click()

time.sleep(5)  

element = WebDriverWait(driver, 7).until(  
    EC.element_to_be_clickable((By.ID, 'bigCookie'))  
)  

for i in range(50):
    element.click()  


time.sleep(2)  