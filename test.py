import requests
from bs4 import BeautifulSoup

thu_edu_tw = 'http://www.thu.edu.tw'

res = requests.get(thu_edu_tw)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "lxml")
    for i in soup.find_all("div",{"class":"style2"}):
        print(i.h2.text) #取text內容
        for j in i.find_all("a"):
            print(j.text) #取text內容
  
elif res.status_code == 403:
    print("網站拒絕存取")
elif res.status_code == 404:
    print("網站不存在!")
