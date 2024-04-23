import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
import zipfile
import os

## Transform your data
file_path = 'data/data.csv'

companies = []

with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        companies.append(dict(row))

## Download chromedriver
download_url='https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.60/win64/chromedriver-win64.zip'
response = requests.get(download_url)
with open('chromedriver.zip', 'wb') as f:
    f.write(response.content)

zip_path = './chromedriver.zip'
extract_to = './driver'

if not os.path.exists(extract_to):
    os.makedirs(extract_to)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

## Push your data - Go submit to google form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSd3uM0dTtN6sgY3Em-gz8wIZrnfMIZv_BWSSBEOxKzqZLrzyQ/viewform'

options = Options()
options.add_argument('--headless')

service = Service(executable_path='./driver/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

driver.get(form_url)

time.sleep(2)

for entry in companies:
    inputs = driver.find_elements(By.CSS_SELECTOR, '#mG61Hd input[type="text"]')

    company_field = inputs[0]
    employee_count_field = inputs[1]

    company_field.send_keys(entry['Company Name'])
    employee_count_field.send_keys(entry['Number of employees'])

    submit_button = driver.find_element(By.CSS_SELECTOR, 'div[jsname="M2UYVd"]')
    submit_button.click()

    time.sleep(2)

    driver.get(form_url)
    time.sleep(2)

driver.quit()
