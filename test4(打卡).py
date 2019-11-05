from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re, time, datetime


startTime = datetime.datetime(2019, 6, 1, 23, 43, 0)   #設定開始時間
print('Program not starting yet...')
while datetime.datetime.now() < startTime:      #當開始時間小於打卡時間--> 停頓
        #print(datetime.datetime.now())
        time.sleep(1)

option  = webdriver.ChromeOptions()     #利用chrome瀏覽器開啟
#option.add_argument('headless')    #無頭瀏覽
option.add_argument('--ignore-certificate-errors')
#禁止載入圖片
prefs = {"profile.managed_default_content_settings.images": 2}
option.add_experimental_option("prefs", prefs)
#將設定寫入CHROME
driver = webdriver.Chrome(options=option)    

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

driver.find_element_by_id("wp-submit").click()  #點擊送出button(帳號密碼頁)


######################
#    進入系統頁面    #
######################
'''
a1 = driver.switch_to.alert     # 通过switch_to.alert切换到alert
if a1:                          # 如果有alert視窗出現
        a1.accept()             # 等同于点击“确认”或“OK”
'''

driver.find_element_by_id("sign_in1").click()  #點擊button(打卡開始紐)
#driver.find_element_by_id("sign_out1").click()  #點擊button(打卡結束紐)
driver.close()


endTime = datetime.datetime(2019, 8, 1, 16, 00, 0)     #設定結束時間
while datetime.datetime.now() < endTime:                #當現在時間小於結束時間--> 停頓
	time.sleep(1)

option  = webdriver.ChromeOptions()     #利用chrome瀏覽器開啟
#option.add_argument('headless')    #無頭瀏覽
option.add_argument('--ignore-certificate-errors')
#禁止載入圖片
prefs = {"profile.managed_default_content_settings.images": 2}
option.add_experimental_option("prefs", prefs)
#將設定寫入CHROME
driver = webdriver.Chrome(options=option)    

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

driver.find_element_by_id("wp-submit").click()  #點擊送出button(帳號密碼頁)

driver.find_element_by_id("sign_out1").click()  #點擊button(打卡結束紐)

