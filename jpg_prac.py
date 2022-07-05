import time
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
JPG_PATH = 'https://www.jpg.store/collection/cornucopias-land-zones'

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
corn = {}
tier = ['CM', 'UC', 'RA', 'LE', 'MY']
size = ['small', 'medium', 'large', 'epic', 'copias']
driver.get(JPG_PATH)
while(1):
    time.sleep(3)
    for s in size:
        print("==== {} ====".format(s))
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="collectionSearch"]' )))
        #WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.ID,'collectionSearch' )))
        find_bar = driver.find_element(By.ID, 'collectionSearch')
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