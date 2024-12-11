from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
query = 'Dhaka'
driver.get(f"https://www.google.com/search?q={query}")
elems = driver.find_elements(By.CSS_SELECTOR, "li.sbct")
for elem in elems:
    scrapt_data = elem.get_attribute('outerHTML')
    with open(f"data/scrapt.html",'w', encoding='utf-8') as f:
        f.write(scrapt_data)
    

time.sleep(.06)
driver.close()