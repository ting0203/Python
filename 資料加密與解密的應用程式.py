#**********************************************
# Name: 吳宜庭
# Class: 資管三
# SID: S05490055
# Function:
#           (1). 從鍵盤上輸入欲加密之正整數資料與欲解密之正整數資料。
#           (2). 進行加密解密動作。
#           (3). 取得程式執行所需的時間。
#           (4). 將(2)(3)的結果列印於螢幕上。
# Homework: No.1
# Limitations:
#           (1).加解密的正整數(其值介於0000至9999)
# Date: 2018/10/03
#**********************************************

import time                                             #引入時間模組
start = time.time()                                     #將start標籤指向開始時間的物件
#==========印出此程式名稱，個人資料=========#
print("""                                               
****************************************           
*       資料加密與解密的應用程式       *
*       資管三 吳宜庭  S05490055       *
****************************************
""")

#==========將unen_num標籤 指向輸入之字串==========
unen_num=input("請輸入一個四位數未經加密的正整數資料：")     
print()
#=====將n_key標籤指向輸入之整數並轉換成整數型態=====
n_key=int(input("請輸入key值(1至9之間的整數):"))        
print() 

#===將num1,2,3,4標籤指向unen_num第n個位置並傳換成整數型態進行加密===
num1 = ((int(unen_num[0]))+n_key)%10                         
num2 = ((int(unen_num[1]))+n_key)%10
num3 = ((int(unen_num[2]))+n_key)%10
num4 = ((int(unen_num[3]))+n_key)%10
#=====印出加密後數字，以格式化輸出=====
print('加密後的資料：%d%d%d%d\n' % (num4,num3,num2,num1))

#==========將en_num標籤 指向輸入之字串==========
en_num=input("請輸入一個四位數已經加密的正整數資料：")
print()
#===將num1,2,3,4標籤指向en_num第n個位置並傳換成整數型態進行解密===
num1=(((int(en_num[0]))+10)-n_key)%10
num2=(((int(en_num[1]))+10)-n_key)%10
num3=(((int(en_num[2]))+10)-n_key)%10
num4=(((int(en_num[3]))+10)-n_key)%10
#=====印出解密後數字，以格式化輸出=====
print('解密後的資料：%d%d%d%d\n'% (num4,num3,num2,num1))

stop = time.time()                                          #stop標籤指向停止時間的物件
exec_duration = stop-start                                  #exec_duration標籤指向stop-start的結果
print("程式結束，本程式執行時間長度為 %f 秒\n" %exec_duration)    #印出exec_duration指向的結果
#===========================================================
# =========== 結束程式的執行 ============ #
input('Please enter any key to exit...')                    
