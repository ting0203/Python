#**********************************************
# Name: 吳宜庭
# Class: 資管三
# SID: S05490055
# Program Name: hw4_2.py
# Function:(1)宣告學生基本資料：系所、年級、學號、姓名
#          (2)記錄每科成績：經濟、會計、統計、管概 、計概與程設
#          (3)紀錄平均分數、最高分科目與最低分科目
#          (4)印出學生系所、年級、姓名、每科科目成績、平均分數、最高分科目與最低分科目
#          (5) 宣告計算學生個人平均成績的方法或行為
#          (6) 宣告可找出學生個人最高分科目與成績的方法或行為
#          (7) 宣告可找出學生個人最低分科目與成績的方法或行為
# Homework: No.4
# Limitations: (1). 需將成績排序(由高至低)
#              (2). 成績需用已設定好數值
# Date: 2018/12/04
# **********************************************

#=====宣告學生方法=====
class student():
    #=====將資料(系別，年級，學號，姓名，成績)傳入，成績以字典方式儲存=====
    def __init__(self,dept,grade,std_id,name,score):
        self.dept=dept
        self.grade=grade
        self.name=name
        self.std_id=std_id
        self.score={'經濟成績':score[0],'會計成績':score[1],'統計成績':score[2],'管概成績':score[3],'計概成績':score[4],'程設成績':score[5]}

    #=====排序(由大到小)，用字典的value去做排序，在使用reverse反轉=====
    def m_sort(self):
        self.score = sorted(self.score.items() ,key=lambda x:x[1], reverse=True)

    #=====印出排序過的所有成績=====
    def print_score(self):
        for a,b in self.score:
            print("\t%s: %d" % (a,b))

    #=====印出最高分成績，因做過排序，故在score第0的位置即為最高分=====
    def higher_score(self):
        print("\t最高分: %s: %d" % (self.score[0]))

    #=====印出最低分成績，因做過排序，故在score的最後一個即-1的位置為最低分=====
    def lower_score(self):
        print("\t最低分: %s: %d" % (self.score[-1]))
    
    #=====印出平均成績=====    
    def avg_score(self):
        #=====想算平均成績，先將所有分數放入arr_score[]裡=====
        arr_score = []
        for a,b in self.score:
            arr_score.append(b)
        print("\t平均成績: %.2f" % (float(sum(arr_score))/len(arr_score)))
        
    #=====印出所有資料=====
    def print_data(self):
        print("系所: ",self.dept)
        print("年級: ",self.grade)
        print("姓名: ",self.name)
        self.m_sort()
        self.print_score()
        self.lower_score()
        self.higher_score()
        self.avg_score()
        print()

#=====將每位學生的成績指給個別的score物件=====
score1 = (66,15,33,28,89,92)
score2 = (78,25,63,58,73,46)
score3 = (34,66,71,98,44,25)

#=====stu1使用student方法，並將資料傳入=====
stu1=student('資管系','大二','S01234567','馬悠悠',score1)
stu1.print_data()

#=====stu2使用student方法，並將資料傳入=====
stu2=student('企管系','大三','S02345678','無飽春',score2)
stu2.print_data()

#=====stu3使用student方法，並將資料傳入=====
stu3=student('財經系','大四','S03456789','林志霖',score3)
stu3.print_data()

input('Please Enter any key to exit...')



