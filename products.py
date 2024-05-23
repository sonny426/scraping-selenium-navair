from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()

data = []

for i in range(0, 11):
    print(i)
    driver.get("https://www.navair.navy.mil/ProductContent?page="+str(i))

    elements = driver.find_elements(By.CLASS_NAME, "card")
    links = []

    for element in elements:
        a_tag = element.find_element(By.TAG_NAME, 'a')
        links.append(a_tag.get_attribute('href'))

    for link in links:
        driver.get(link)
        title = driver.find_element(By.CLASS_NAME, 'paper-canvas').find_element(By.TAG_NAME, 'h2').text
        description = driver.find_element(By.CLASS_NAME, 'paper-canvas').find_element(By.CLASS_NAME, 'field--name-body').find_element(By.TAG_NAME, 'p').text
        print(description)
        data.append({"url":link, "title":title, "description":description})

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)