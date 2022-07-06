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
    tier = corn['property']['tier']
    size = corn['property']['size']
    driver.get(corn['url'])
    while(1):
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="collectionSearch"]' )))
        #time.sleep(3)
        for s in size:
            print("==== {} ====".format(s))
            #WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.ID,'collectionSearch' )))
            find_bar = driver.find_element(By.ID, 'collectionSearch')
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,'asset-price')))
            driver.implicitly_wait(10)
            for t in tier:
                txt = '{} land plot claim {}'.format(s, t)
                find_bar.send_keys(txt)
                #WebDriverWait(driver, 100).until(EC.element_to_be_selected((By.XPATH,'//*[@id="asset-price"]' )))
                el = WebDriverWait(driver, 5).until(EC.staleness_of(driver.find_element(By.ID,'asset-price')))
                #time.sleep(2)
                #WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#marketplace > div.infinite-scroll-component__outerdiv > div > div.styles_customLoaderContainer__REOt4')))
                price = driver.find_element(By.ID, 'asset-price').text
                #el = WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID,'asset-price')))
                for i in range(len(txt)):
                    find_bar.send_keys(Keys.BACKSPACE)
                    #el = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#marketplace > div.infinite-scroll-component__outerdiv > div > div.styles_customLoaderContainer__REOt4')))
                print('{} : {}'.format(t, price))
                #el = WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#marketplace > div.infinite-scroll-component__outerdiv > div > div.styles_customLoaderContainer__REOt4')))
                #el = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'asset-price')))
        print("==============")
    driver.quit()

if __name__=="__main__":
    main()