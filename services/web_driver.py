import os
import zipfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriver:
    def __init__(self, driver_zip_path='./chromedriver.zip', driver_path='./driver/chromedriver-win64/chromedriver.exe'):
        self.driver_zip_path = driver_zip_path
        self.driver_path = driver_path
        self.driver = None
        self._extract_driver()

    def _extract_driver(self):
        extract_to = os.path.dirname(self.driver_path)
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        with zipfile.ZipFile(self.driver_zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    def start(self, headless=True):
        options = Options()
        if headless:
            options.add_argument('--headless')

        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def navigate(self, url):
        if self.driver is None:
            raise Exception("Driver not started. Call start() first.")

        self.driver.get(url)
        time.sleep(2)  # wait for page to load

    def quit(self):
        if self.driver is not None:
            self.driver.quit()