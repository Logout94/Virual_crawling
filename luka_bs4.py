import os
import sys
import requests
from bs4 import BeautifulSoup

url = 'https://luka7.net/'
def main():
    rs = requests.get(url)

    if rs.status_code == 200:
        html = rs.content
        soup = BeautifulSoup(html, 'html.parser')
        lst = soup.select("div.inner p > span#USDKRW")
        print(lst)
if __name__=='__main__':
    main()