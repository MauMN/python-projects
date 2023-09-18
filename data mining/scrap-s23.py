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

    driver.get("https://www.mercadolibre.com.ar/samsung-galaxy-s23-ultra-12gb-256gb-color-cream/p/MLA21394678?pdp_filters=category:MLA1055#searchVariation=MLA21394678&position=1&search_layout=stack&type=product&tracking_id=e1d71c77-b617-4f4e-bf06-6cbbb2b14d52")
    time.sleep(2)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER).perform()

    #driver.implicitly_wait(10)

    return driver

driver = launchBrowser()

div_element = driver.find_elements(By.CLASS_NAME, "ui-review-capability-comments__comment__content")

all_comments = ""

for i in div_element:
    contenido = i.text
    all_comments = all_comments + str(contenido) + os.linesep

print(all_comments)

with open(CUR_DIR/"datoscomments.txt", "w", encoding='utf-8') as file:
    file.write(all_comments)