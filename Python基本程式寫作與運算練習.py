#********************************************************
# Name: 吳宜庭
# Class: 資管三
# SID: s05490055
# Program Name: s05490055.py
# Function: (1) 產生一個fruits串列
#           (2) 利用所指定的指令產生出rep1_fruits、rep2_fruits串列
#           (3) 利用指定的指令移除物件
#           (4) 將串列轉換成元組，計算出有幾個指定物件及其索引值和是否出現在此元組中
# Homework: No.2
# Limitations: (1). 限定使用已教過的Python指令語法
# Date: 2018/10/13
#********************************************************

print('''
************************************************

*            107-1 HW2 程式輸出報表            *

************************************************
''')
#=====將fruits標籤指定給一個串列=====
fruits = ['apple', 'pineapple', 'banana', 'grape', 'orange', 'watermelon']
#=====印出第一個執行結果=====
print("(1) Answer:\n")
print("fruits = ",fruits)

#=====將rep1_fruits標籤指定給fruits各索引值不同的內容相加成的串列=====
rep1_fruits = fruits[:3] + fruits[1:2] + fruits[2:4]*2 + fruits[4:5] + fruits[3:6]
#=====印出第二個執行結果=====
print("\n(2) Answer:\n")
print("rep1_fruits = ",rep1_fruits)

#=====使用extend方法將add串列裡的內容加到f1串列(內容為fruits的前三個)裡，再將rep2_fruits標籤指向f1串列=====
f1 = fruits[:3]
add = ['pineapple'] + fruits[2:4]*2 + ['orange'] + fruits[3:6]
f1.extend(add)
rep2_fruits = f1
#=====印出第三個執行結果=====
print("\n(3) Answer:\n")
print("rep2_fruits = ",rep2_fruits)

#=====印出第四個執行結果，先印出原串列rep1_fruits=====
print("\n(4) Answer:\n")
print("Original list :\nrep1_fruits = ",rep1_fruits)
#=====將rep1_fruits第二個索引值的值刪除，印出結果=====
del rep1_fruits[2]
print("\nDelete the first 'banana':\nrep1_fruits = ",rep1_fruits)
#=====將rep1_fruits第三個索引值的值刪除，印出結果=====
del rep1_fruits[3]
print("\nDelete the second 'banana':\nrep1_fruits = ",rep1_fruits)
#=====將rep1_fruits第四個索引值的值刪除，印出結果=====
del rep1_fruits[4]
print("\nDelete the third 'banana':\nrep1_fruits = ",rep1_fruits)
#=====將rep1_fruits裡的grape移除，印出結果=====
rep1_fruits.remove('grape')
print("\nRemove the first 'grape' from the list:\nrep1_fruits = ",rep1_fruits)
rep1_fruits.remove('grape')
print("\nRemove the second 'grape' from the list:\nrep1_fruits = ",rep1_fruits)
rep1_fruits.remove('grape')
print("\nRemove the third 'grape' from the list:\nrep1_fruits = ",rep1_fruits)

#=====印出第五個執行結果，先印出原串列rep2_fruits=====
print("\n(5)Answer:\n")
print("Original list :\nrep2_fruits = ",rep2_fruits)
#=====將rep2_fruits最後一個值移除，在印出結果=====
rep2_fruits.pop()
print("\nPop the last object named 'watermelon' off the list :\nrep2_fruits = ",rep2_fruits)
rep2_fruits.pop()
print("\nPop the last object named 'orange' off the list :\nrep2_fruits = ",rep2_fruits)
#=====將rep2_fruits從後面數來第二個值移除，在印出結果=====
rep2_fruits.pop(-2)
print("\nPop the object named 'orange' off the list :\nrep2_fruits = ",rep2_fruits)

#=====印出第六個執行結果，將rep3_fruits標籤指向rep2_fruits串列轉成元組=====
print("\n(6)Answer:")
rep3_fruits = tuple(rep2_fruits)
print("\nrep3_fruits = ",rep3_fruits)
#=====將num標籤指向pinapple在rep3_fruits裡的個數(用count方法)，並印出結果=====
num = rep3_fruits.count('pineapple')
print("\nThere are",num,"object named 'pineapple' in the rep3_fruits.")
#=====將index標籤指向pinapple在rep3_fruits裡的索引值(用index方法)，並印出結果=====
index = rep3_fruits.index('pineapple')
print("\nThe index of the first object named 'pinapple' in the rep3_fruits is",index)
#=====印出banana和orange是否存在rep3_fruits裡，印出結果=====
print("\nIs the object named 'banana' in the rep3_fruits ? : ",'banana' in rep3_fruits)
print("\nIs the object named 'orange' in the rep3_fruits ? : ",'orange' in rep3_fruits)
input("\nPlease enter any key to exit ...")
