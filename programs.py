from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

driver = webdriver.Chrome()

data = []

driver.get("https://www.secnav.navy.mil/rda/Pages/Programs.aspx")

elements = driver.find_element(By.ID, "progList").find_elements(By.TAG_NAME, "a")

links = []

for element in elements:
    href = element.get_attribute('href')
    print(href)
    if href == '#':
        continue
    links.append({"url":href,"title":element.get_attribute('innerHTML')})

for link in links:
    driver.get(link["url"])
    print(link)
    try:
        description=driver.find_element(By.CLASS_NAME, "wholeContent").text
        data.append({"url":link["url"], "title":link["title"], "description":description})
    except:
        print("Element not found")
 

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)