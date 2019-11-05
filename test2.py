from bs4 import BeautifulSoup
from selenium import webdriver
import re

option  = webdriver.ChromeOptions()
#option.add_argument('headless')
option.add_argument('--ignore-certificate-errors')
#禁止載入圖片
prefs = {"profile.managed_default_content_settings.images": 2}
option.add_experimental_option("prefs", prefs)
#將設定寫入CHROME
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://arcanegs.000webhostapp.com/test.html") #欲抓取網站的路徑

soup = BeautifulSoup(driver.page_source, "lxml") #藉由BeautifulSoup分析擷取資料
print(soup)
