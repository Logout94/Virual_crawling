from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER_PATH = '/Users/leewan/driver/chromedriver'

chrome_options= webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(3)

driver.get('https://luka7.net')
USD = driver.find_element(By.ID, 'USDKRW')
print(USD.text)