# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:02:32 2020

@author: zhoubo
"""
from matplotlib import pyplot as plt

#---------------------设置中文字体----------------
import matplotlib
font = {'family' : 'MicroSoft YaHei',
              'weight' : 'bold',
              'size'   : '5'}
matplotlib.rc('font',**font)
#------------------------------------------------
-

y_3 =[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 =[i for i in range(1,32)]
x_10 =[i for i in range(32,63)]

x= x_3+x_10

x3_ticks = ['3月{}日'.format(i) for i in x_3[:30]]
x10_ticks =['11月{}日'.format(i-31) for i in x_10[:]]

x_ticks =x3_ticks + x10_ticks

#标题 刻度名字三件套
plt.title('月份-降雨天数 图',fontsize =12)
plt.xlabel('月份',fontsize =12)
plt.ylabel("降雨天数",fontsize =12)



#绘制散点图 折线图是plot 散点图是scatter
plt.scatter(x_3,y_3,label='3月份')
plt.scatter(x_10,y_10,label ='10月份')

plt.xticks(x[::3],x_ticks[::3],rotation =45)

#添加图例  一般调整个位置就ok了
plt.legend(loc =2)


plt.show()