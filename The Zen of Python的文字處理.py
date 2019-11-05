#**********************************************
# Name: 吳宜庭
# Class: 資管系三年級
# SID: S05490055
# Program Name: hw3.py
# Function: (1) 將以加密過的文字作解密
#           (2) 將解密完的結果再加密回去，再做比對，若完全無誤輸出"加密內容經比對後正確無誤！"
#           (3) 計算並顯示執行解密之後原文中的字元個數
#           (4) 將解密之後的原文做文字處理並將結果顯示列印出來
#           (5) 顯示完成時的年月時分秒
#           (6) 個人姓名學號
# Homework: No.3
# Limitations: (1). 若function(2)比對結果不正確則表示程式有誤，務必修正。
# Date: 2018/10/30
# **********************************************

import datetime     # 匯入datetime模組

print('''*************************************
*                                   *
*      107-01 HW3 程式輸出報表      *
*      資管三 吳宜庭 HW3  程式      *
*                                   *
*************************************
''')

# 以加密過的字串指給s標籤 #
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

# 將d宣告為空字典 #
d = {}

# =============================================================== #
# 將每一個英文字加上13進行加密，並放入字典d裡面					  #
# (從ascii碼65'A'開始26個與從ascii碼97'a'開始26個英文字)		  #
# =============================================================== #
for c in (65, 97): 
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
        
# =================================================================================== #
# 印出(a)小題，將解密後的文字印出													  #
# 將已解密的文字指給unenstr標籤														  #
# 用for迴圈從s字串裡讀到的每一個字去d字典裡面找到對應的後回傳它的值再用join加到字串   #
# =================================================================================== #
unenstr="".join([d.get(c, c) for c in s])
print(">>(a)小題：顯示解密的原文內容")
print(unenstr,"\n")

# ===============================================================================   #
# 印出(b)小題，將解密後的文字再加密回去，並與原字串s比較內容，若無誤則印出題目所說  #
# ===============================================================================   #
print(">>(b)小題：比對'再加密之後的字串'與'解密前的字串'內容是否相同無誤")

# ======================================================================================= #
# 用for迴圈從unenstr字串裡讀到的每一個字去d字典裡面找到對應的後回傳它的值再用join加到字串 #
# 用if去將(s已加密字串)與(unenstr解密後字串再加密回去的字串)做比較						  #
# ======================================================================================= #
if s=="".join([d.get(c, c) for c in unenstr]):
    print("比對結果：加密內容經比對後正確無誤！\n")
else:
    print("1")

# ============================== #
# 印出(c)小題，顯示出總字數	 	 #
# ============================== #
print(">>(c)小題：計算並顯示(a)解密之後原文中的字元個數(包含標點符號與空白)")
print("原文解密後的字元個數",len(unenstr),"\n")

# =============================================================================================================== #
# 印出(d)小題，宣告w為字典放入從unenstr裡讀取到的字與這個字被讀取過的次數										  #
# 使用for迴圈，將unenstr轉型為集合再從中用word去放讀取的字，再放入w字典的key且對應的value為出現次數 用count計算   #
# =============================================================================================================== #
print(">>(d)小題：將(a)解密之後的原文做(1)字元分類(2)計算相同字元出現的次數\n字元分類與出現個數：\n")
print("         字元  :  出現次數\n        =================\n")
w={word:unenstr.count(word) for word in set(unenstr)}

# ================================================================================ #
# 將w字典裡的key做排序且用tuple去放讀到的值與在w裡對應到的值，且全部加到ss串列裡   #
# ================================================================================ #
ss = [(k,w[k]) for k in sorted(w.keys())]

# ================================================================= #
# 將ss串列裡的資料讀出並印出，若遇到'\n'則用if判斷(使用ascii判斷)   #
# ================================================================= #
for key,value in ss:
    if ord(key)==10:
        print("         '\\n'  :   %3d" %(value))
    else:
        print("         '%s'   :   %3d" %(key,value))

# ============================ #
# 印出完成執行的年月時分秒	   #
# ============================ #
print("\n>>(e)小題：",datetime.datetime.now(),"\n")

# =========== 結束程式的執行 ============ #
input('Please enter any key to exit...')  
