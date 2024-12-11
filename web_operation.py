from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup
import os 

def web_to_scripting_operation(query):

    file_path = 'data/scrapt.html'
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/?hl=en")

    # Find the search box element
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)

    # Wait for suggestions to load
    time.sleep(2)

    # Fetch the suggestion elements
    suggestions = driver.find_elements(By.CSS_SELECTOR, "div.lnnVSe")

    # Extract and print the suggestion texts
    for suggestion in suggestions:
        scrapt_data = suggestion.get_attribute('outerHTML')
        with open(file_path,'a', encoding='utf-8') as f:
            f.write(scrapt_data)
    # Close the browser
    on_html_operation(file_path)
    if os.path.exists(file_path):
        os.remove(file_path) 
    driver.quit()

def on_html_operation(file_path):
    with open(file_path,'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc,'html.parser')
    
    longest_option = ''
    shortest_option = ''
    elements = soup.find_all('div', class_='lnnVSe')
    for element in elements:
        # flag = 0
        title = element.find('div',class_='wM6W7d')
        # if title:
            # print(title.text)
        description = element.find('div',class_='ClJ9Yb')
        # if description:
            # print(description.text)
        if title and description:
            if len(title.text) > 1 or len(description.text) > 1:
                text = f"{title.text} {description.text}"
                # if flag == 0:
                #     shortest_option = text
                if len(text) > len(longest_option):
                    longest_option = text
                # print(f'sortest option time: {shortest_option}, {len(shortest_option)}')
                if not shortest_option or len(text) < len(shortest_option):
                    # print(f"ver:{len(shortest_option)} tex: {len(text)}")
                    shortest_option = text
                print(f'full text: {text}')
        # flag += 1
    print(f"Longest path: {longest_option}")
    print(f"shortest_option : {shortest_option}")