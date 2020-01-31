# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:06:00 2020

@author: zhoubo
"""

#多个条形图对比
from matplotlib import pyplot as plt
import matplotlib


font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold',
        'size'   : '8'}
matplotlib.rc('font',**font)

#设置图像大小
plt.figure(figsize=(16,8),dpi = 80)


a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

#如何直观的显示3天的数据？
x_14 =list(range(len(a)))
x_15 =[i+0.2 for i in x_14]
x_16 =[i+0.2+0.2 for i in x_14]

plt.bar(x_14,b_14,width =0.2,label ='14日'  )
plt.bar(x_15,b_15,width =0.2,label ='15日' )
plt.bar(x_16,b_16,width =0.2,label ='16日')


plt.title('三天票房分布',fontsize =20)

plt.xticks(x_15,a,fontsize =15)
plt.legend()

plt.show()