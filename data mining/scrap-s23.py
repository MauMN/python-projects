from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

from pathlib import Path
CUR_DIR = Path(__file__).resolve().parent

import time
import os

def launchBrowser():
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.amazon.com/-/es/Tel%C3%A9fono-inteligente-desbloqueado-almacenamiento-estadounidense/dp/B0BLP2B5DZ?th=1")
    time.sleep(2)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER).perform()

    driver.implicitly_wait(10)

    return driver

driver = launchBrowser()
driver.maximize_window()

see_more_button = driver.find_element(By.XPATH, '//*[@id="reviews-medley-footer"]/div[2]/a')
see_more_button.click()

div_element = driver.find_elements(By.CLASS_NAME, "cr-original-review-content")

all_comments = ""

for i in div_element:
    contenido = i.text
    all_comments = all_comments + str(contenido) + os.linesep

#print(all_comments)

with open(CUR_DIR/"datoscomments.txt", "w", encoding='utf-8') as file:
    file.write(all_comments)