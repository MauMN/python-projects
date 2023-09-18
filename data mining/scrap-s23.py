from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

import time

def launchBrowser():
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.mercadolibre.com.ar/samsung-galaxy-s23-ultra-12gb-256gb-color-cream/p/MLA21394678?pdp_filters=category:MLA1055#searchVariation=MLA21394678&position=1&search_layout=stack&type=product&tracking_id=e1d71c77-b617-4f4e-bf06-6cbbb2b14d52")
    time.sleep(2)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER).perform()

    while(True):
       pass

launchBrowser()