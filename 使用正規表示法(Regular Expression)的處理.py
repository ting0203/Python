#**********************************************
# Name: 吳宜庭
# Class: 資管三
# SID: S05490055
# Program Name: hw5.py
# Function: 在Python中使用正規表示法的處理
# Homework: No.5
# Limitations: (1). 從鍵盤上輸入任意一個英文字串，且輸入的字串必須包含至少
#                   三個(≥3)以上的英文單字，單字之間以空格隔開
#              (2). 如輸入少於三個以上的英文單字，程式會要求
#                   重新輸入直到正確為止。
# Date: 2018/12/16
# **********************************************

import re   #引入re模組

#=====       輸入一字串，並顯示出P1-8的結果        =====
#=====           要自行輸入請解開下方註解          =====
#=====判斷str1的單字個數是否超過3個，若否則持續輸入=====

#str1 = input("***The input string => ")
str1='This is an apple'
print('***The input string => This is an apple')
print()
list1=re.split(' ',str1)
while len(list1) < 3:
    str1 = input("***The input string => ")
    list2=re.findall('\S+',str1)
    if len(list2) >= 3:
        break
#使用模組re的函式findall,截取str1中每一個字元
print("[P-1] Output:\n",re.findall('\D',str1),'\n')

#使用模組re的函式findall,截取str1中每一個字元但去除空白/格字元
print("[P-2] Output:\n",re.findall('\S',str1),'\n')

#使用模組re的函式findall,截取str1中每一個單字包含空格
print("[P-3] Output:\n",re.findall('\w*',str1),'\n')

#使用模組re的函式findall,截取str1中每一個單字包含空格但只截取字串中每一個單字
print("[P-4] Output:\n",re.findall('\S+',str1),'\n')

#使用模組re的函式findall,截取str1中的第一個單字
print("[P-5] Output:\n",re.findall('^[A-Z]+[A-Za-z]+',str1),'\n')

#使用模組re的函式findall,截取str1中的最後一個單字
print("[P-6] Output:\n",re.findall('[A-Za-z]+$',str1),'\n')

#使用模組re的函式findall,截取str1中每一個單字的前二個字元
print("[P-7] Output:\n",re.findall(r'\b\S{2}',str1),'\n')

#使用模組re的函式findall,擷取str1中每一個單字的開始是母音(aeiouAEIOU)的字元
print("[P-8] Output:\n",re.findall(r'\b[AEIOUaeiou]\w+',str1),'\n')


#=====      輸入一字串，並顯示出P9-12的結果           =====
#=====          要自行輸入請解開下方註解              =====
#=====判斷str2裡的email地址是否超過3個，若否則持續輸入=====

#str2 = input("***The input email address => ")
str2='s102356@gmail.com, cia@test.gov.us, john_123@winworld.com, first.test@travel.biz'
print('***The input string => s102356@gmail.com, cia@test.gov.us, john_123@winworld.com, first.test@travel.biz')
print()
list1=re.findall('[@]\w+',str2)
while len(list1) < 3:
    str2 = input("***The input email address => ")
    list2=re.findall('[@]\w+',str2)
    if len(list2) >= 3:
        break

#使用模組re的函式findall,截取str1中每一個email位址中的組織名稱
print("[P-9] Output:\n",re.findall('[@]\w+',str2),'\n')

#使用模組re的函式findall,截取str1中每一個email位址中的組織名稱與網域類別
print("[P-10] Output:\n",re.findall('[@]\w+[.]\w+',str2),'\n')

#使用模組re的函式findall,截取str1中每一個email位址中的網域類別名稱
print("[P-11] Output:\n",re.findall('@\w+.(\w+)',str2),'\n')

#使用模組re的函式findall,截取str1中每一個email位址中的使用者名稱/ID
print("[P-12] Output:\n",re.findall('(\S+)@',str2),'\n')

#=====      輸入一字串，並顯示出P13-14的結果         =====
#=====          要自行輸入請解開下方註解             =====
#=====判斷str3裡的日期資訊是否超過3個，若否則持續輸入=====
#str3 = input("***The input email address => ")
str3='LIZ 88-1057 12-07-1998, XYZ 56-7893 12-10-2014, ABC 99-0111 05-31-2017'
print('***The input string => LIZ 88-1057 12-07-1998, XYZ 56-7893 12-10-2014, ABC 99-0111 05-31-2017')
print()
list1=re.findall('\d\d-\d\d-\d\d\d\d',str3)
while len(list1) < 3:
    str3 = input("***The input email address => ")
    list2=re.findall('\d\d-\d\d-\d\d\d\d',str3)
    if len(list2) >= 3:
        break

#使用模組re的函式findall,截取str1中每一個日期資訊
print("[P-13] Output:\n",re.findall('\d\d-\d\d-\d\d\d\d',str3),'\n')

#使用模組re的函式findall,截取str1中每一個日期資訊中的年份
print("[P-14] Output:\n",re.findall('\d\d-\d\d-(\d\d\d\d)',str3),'\n')



