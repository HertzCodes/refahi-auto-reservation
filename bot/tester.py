from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
# service = Service(executable_path="chromedriver.exe")
chromedriver_autoinstaller.install()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def call_website(x):
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/")
x = [0 for i in range(15)]
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(call_website, x)