#**********************************************
# Name: 吳宜庭
# Class: 資管三
# SID: s05490055
# Program Name: hw4_1.py
# Function: (1)有四類別：圓形，長方形，梯形，三角形
#           (2)計算其面積和周長
# Homework: No.4
# Limitations: (1)限用已教過的python指令語法
# Date: 2018/12/01
# **********************************************

#=======圓形類別=======
class circle():
    def __init__(self,name,radius):
        self.name = name
        self.radius = radius
    #=======計算周長=======
    def c_perimeter(self):
        return 2*self.radius*3.1415
    #=======計算面積=======
    def c_area(self):
        return self.radius**2*3.1415

#=======長方形類別=======
class rectangle():
    def __init__(self,name,lenght,width):
        self.name=name
        self.lenght=lenght
        self.width=width
    #=======計算周長=======
    def rec_perimeter(self):
        return (self.lenght+self.width)*2
    #=======計算面積=======
    def rec_area(self):
        return self.lenght*self.width

#=======梯形類別=======
class trapezoid():
    def __init__(self,name,topline,baseline,height):
        self.name=name
        self.topline=topline
        self.baseline=baseline
        self.height=height
    #=======計算面積=======
    def tra_area(self):
        return ((self.topline+self.baseline)*self.height)/2

#=======三角形類別=======
class triangle():
    def __init__(self,name,baseside,height):
        self.name=name
        self.baseside=baseside
        self.height=height
    #=======計算面積=======
    def tri_area(self):
        return (self.baseside*self.height)/2

#=======a,b物件用cicle類別呼叫，帶入名字與半徑=======
a=circle('圓形物件一',5)
print('%s\n\t面積：%.2f平方公分\n\t周長：%.2f公分\n' %(a.name,a.c_area(),a.c_perimeter()))

b=circle('圓形物件二',12.5)
print('%s\n\t面積：%.2f平方公分\n\t周長：%.2f公分\n' %(b.name,b.c_area(),b.c_perimeter()))

#=======c,d物件用rectangle類別呼叫，帶入名字、長與寬=======
c=rectangle('長方形物件一',6,100)
print('%s\n\t面積：%.2f平方公分\n\t周長：%.2f公分\n' %(c.name,c.rec_area(),c.rec_perimeter()))

d=rectangle('長方形物件二',13,62)
print('%s\n\t面積：%.2f平方公分\n\t周長：%.2f公分\n' %(d.name,d.rec_area(),d.rec_perimeter()))

#=======e,f物件用trapezoid類別呼叫，帶入名字、上底、下底與高=======
e=trapezoid('梯形物件一',15,20,6)
print('%s\n\t面積：%.2f平方公分\n' %(e.name,e.tra_area()))

f=trapezoid('梯形物件二',8,60,18)
print('%s\n\t面積：%.2f平方公分\n' %(f.name,f.tra_area()))

#=======g,h物件用triangle類別呼叫，帶入名字、底與高=======
g=triangle('三角形物件一',13,8)
print('%s\n\t面積：%.2f平方公分\n' %(g.name,g.tri_area()))

h=triangle('三角形物件二',21.5,18)
print('%s\n\t面積：%.2f平方公分\n' %(h.name,h.tri_area()))

input('Press any key to exit...')

