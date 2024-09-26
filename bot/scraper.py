from concurrent.futures import ThreadPoolExecutor

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()


def start_scraping(args):
    username = args[0]
    password = args[1]
    driver = webdriver.Chrome()
    driver.get("http://refahi.kntu.ac.ir/")
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "btn-redirect-cancel")))

    decline_button = driver.find_element(By.ID, "btn-redirect-cancel")
    decline_button.click()

    user_field = driver.find_element(By.NAME, "username")
    user_field.send_keys(username)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password + Keys.ENTER)

    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@class='icon']/span[1]")))
    reserve_btn = driver.find_element(By.XPATH, "//div[@class='icon']/span[1]")
    reserve_btn.click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, 'selectedSelfDefIdCombo')))
    select_faculty_dropdown = driver.find_element(By.NAME, 'selectedSelfDefIdCombo')
    select_faculty_dropdown.click()

    select_option = driver.find_element(By.XPATH, "//select[@name='selectedSelfDefIdCombo']/option[5]")
    select_option.click()

    accept_btn = driver.find_element(By.CSS_SELECTOR, "input.ui-button.ui-widget")
    accept_btn.click()


if __name__ == "__main__":
    x = [('usr', 'pass') for i in range(100)]
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(start_scraping, x)
