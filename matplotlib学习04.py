# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:18:53 2020

@author: zhoubo
"""

#条形图绘制

from matplotlib import pyplot as plt
import matplotlib


font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold',
        'size'   : '8'}
matplotlib.rc('font',**font)

#设置图像大小
plt.figure(figsize=(16,8),dpi = 80)




a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5\n：最后的骑士","摔跤吧！\n爸爸","加勒比海盗5\n：死无对证","金刚\n：骷髅岛","极限特工\n：终极回归","生化危机6\n：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3\n：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23] 


#---------------------------创建（正常，竖着的）条形图用 bar-------------------- 

# plt.bar(range(len(a)),b,color = 'orange')

#------------------------------------------------------------------------------



#---------------------------创建横着的条形图 用 barh---------------------------- 
plt.barh(range(len(a)),b,color = ['orange','blue','black','green','red'],height =0.8)#竖条形图宽度height

plt.grid(alpha =0.4)

#plt.xticks(range(len(a)),a,rotation =90)


plt.yticks(range(len(a)),a)

plt.show()