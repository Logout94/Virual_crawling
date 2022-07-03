import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER_PATH = '/Users/leewan/driver/chromedriver'

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://luka7.net')
WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#coinList > div.row.val.ADA > div.krw")))
while(1):
    time.sleep(3)
    USD = driver.find_element(By.ID, 'USDKRW').text
    coinList = driver.find_element(By.ID, 'coinList')
    #ADA_KRW = ADA.find_element(By.CLASS_NAME, 'krw')
    ADA = coinList.find_element(By.CLASS_NAME, 'ADA')
    print(ADA.find_element(By.CLASS_NAME, 'krw').text)

    #print(ADA_USD)

driver.quit()