from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup

def web_to_scripting_operation():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/?hl=en")

    # Find the search box element
    search_box = driver.find_element(By.NAME, "q")

    # Type your query
    query = "Dhaka"
    search_box.send_keys(query)

    # Wait for suggestions to load
    time.sleep(2)

    # Fetch the suggestion elements
    suggestions = driver.find_elements(By.CSS_SELECTOR, "div.lnnVSe")

    # Extract and print the suggestion texts
    for suggestion in suggestions:
        scrapt_data = suggestion.get_attribute('outerHTML')
        with open(f"data/scrapt.html",'a', encoding='utf-8') as f:
            f.write(scrapt_data)
    # Close the browser
    driver.quit()

def on_html_operation():
    with open(f'data/scrapt.html') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc,'html.parser')
    

    elements = soup.find_all('div', class_='lnnVSe')
    for element in elements:
        title = element.find('div',class_='wM6W7d')
        if title:
            print(title.text)
        description = element.find('div',class_='ClJ9Yb')
        if description:
            print(description.text)
on_html_operation()