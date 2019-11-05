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

driver.get("https://oauth.thu.edu.tw/v1/wp-login.php?redirect_to=%2Fv1%2Findex.php%2Foauth%2Fauthorize%2F%3Fresponse_type%3Dcode%26client_id%3DHbr8NRBfwhwliLtJH0tTqoSjP9Lavm") #欲抓取網站的路徑

soup = BeautifulSoup(driver.page_source, "lxml") #藉由BeautifulSoup分析擷取資料
#print(soup)        #印出為html內容

login = driver.find_element_by_id("user_login")
login.send_keys("S05490055")

password = driver.find_element_by_id("user_pass")
password.send_keys("mc7231266mc")

x = []
data = soup.find_all("span",class_="cptch_span")    #找到所有為span的標籤且class=cptch_span
for s in data:
    x.append(re.findall('\S+',s.get_text()))
#print(x)  ->  x=[['8'], ['×'], ['6'], ['='], []]

if(len(x[0])==0):
    if(x[1][0] == '+'):
        driver.find_element_by_name("cptch_number").send_keys(int(x[4][0])-int(x[2][0]))
    elif(x[1][0] == '−'):
        driver.find_element_by_name("cptch_number").send_keys(int(x[4][0])+int(x[2][0]))
    elif(x[1][0] == "×"):
        driver.find_element_by_name("cptch_number").send_keys(int(x[4][0])//int(x[2][0]))
elif(len(x[2])==0):
    if(x[1][0] == '+'):
        driver.find_element_by_name("cptch_number").send_keys(int(x[4][0])-int(x[0][0]))
    elif(x[1][0] == '−'):
        driver.find_element_by_name("cptch_number").send_keys(int(x[0][0])-int(x[4][0]))
    elif(x[1][0] == "×"):
        driver.find_element_by_name("cptch_number").send_keys(int(x[4][0])//int(x[0][0]))
elif(len(x[4])==0):
    if(x[1][0] == '+'):
        driver.find_element_by_name("cptch_number").send_keys(int(x[0][0])+int(x[2][0]))
    elif(x[1][0] == '−'):
        driver.find_element_by_name("cptch_number").send_keys(int(x[0][0])-int(x[2][0]))
    elif(x[1][0] == "×"):
        driver.find_element_by_name("cptch_number").send_keys(int(x[0][0])*int(x[2][0]))

driver.find_element_by_id("wp-submit").click()  #點擊button
driver.quit()
#sleep(1)
#driver.switch_to.alert.accept()  # 通过switch_to.alert切换到alert

#driver.find_element_by_id("sign_in1").click()  #點擊button

#driver.find_element_by_id("sign_out2").click()  #點擊button





