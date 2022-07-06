from lib2to3.pgen2 import driver
import time
import json
from openpyxl import Workbook
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER_PATH = '/Users/leewan/driver/chromedriver'

def chromeOption():
    chrome_options= webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def jsonLoad(path):
    json_file = open(path)
    project_info = json.load(json_file)
    return project_info

def main():
    driver = chromeOption()
    p_info = jsonLoad('NFT.json')
    corn = p_info['Projects']['Cornucopias']
    pavia = p_info['Projects']['Pavia']
    moon = p_info['Projects']['Moon']

    tier = corn['property']['tier']
    size = corn['property']['size']
    driver.get(corn['url'])
    while(1):
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="collectionSearch"]' )))
        for s in size:
            print("==== {} ====".format(s))
            find_bar = driver.find_element(By.ID, 'collectionSearch')
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,'asset-price')))
            for t in tier:
                txt = '{} land plot claim {}'.format(s, t)
                find_bar.send_keys(txt)
                WebDriverWait(driver, 100).until(EC.staleness_of(driver.find_element(By.ID,'asset-price')))
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,'asset-price')))
                price = driver.find_element(By.ID, 'asset-price').text
                for i in range(len(txt)):
                    find_bar.send_keys(Keys.BACKSPACE)
                print('{} : {}'.format(t, price))
        print("==============")
    driver.quit()

if __name__=="__main__":
    main()