
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re

option  = webdriver.ChromeOptions()     #利用chrome瀏覽器開啟
#option.add_argument('headless')    #無頭瀏覽
option.add_argument('--ignore-certificate-errors')
#禁止載入圖片
prefs = {"profile.managed_default_content_settings.images": 2}
option.add_experimental_option("prefs", prefs)
#將設定寫入CHROME
driver = webdriver.Chrome(chrome_options=option)    

driver.get("https://tixcraft.com/") #欲抓取網站的路徑

soup = BeautifulSoup(driver.page_source, "lxml") #藉由BeautifulSoup分析擷取資料
#print(soup)        #印出為html內容

for i in soup.find_all("li",{"class":"account-login"}):
    #print(i) #取text內容
    driver.find_element_by_link_text('會員登入').click() #點擊頁面上"天氣預報"的連結

sleep(1)
driver.find_element_by_id("loginFacebook").click()

login = driver.find_element_by_id("email")
login.send_keys("fu31lg492002@yahoo.com.tw")

password = driver.find_element_by_id("pass")
password.send_keys("mc7231266mc")

driver.find_element_by_id("loginbutton").click()

'''
x = []
data = soup.find_all("span",class_="cptch_span")    #找到所有為span的標籤且class=cptch_span
for s in data:
    x.append(re.findall('\S+',s.get_text()))driver.find_element_by_id("wp-submit").click()  #點擊button
sleep(1)
driver.switch_to.alert.accept()  # 通过switch_to.alert切换到alert

#driver.find_element_by_id("sign_in1").click()  #點擊button

#driver.find_element_by_id("sign_out2").click()  #點擊button

'''



