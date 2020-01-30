# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:44:48 2020

@author: zhoubo
"""
#%%

from matplotlib import pyplot as plt
import matplotlib


font = {'family' : 'MicroSoft YaHei',
              'weight' : 'bold',
              'size'   : '10.'}
  
matplotlib.rc('font',**font)




nums = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,3,1,1]

years = [i for i in range(11,31)]


#替换x刻度
years_ticks = ['{}岁'.format(i) for i in range(11,31)]

plt.plot(years,nums,'b')
#这一步很重要 你品 你细品
plt.xticks(years[::2],years_ticks[::2],rotation = 90)

plt.xlabel('年龄')
plt.ylabel('交朋友的数量')
plt.title('年龄-交友数量图')

#绘制网格！
plt.grid()
#如果觉得网格太稀疏/密集自己调整下x,y的刻度细密
plt.grid(alpha = 0.2)#调整网格透明度

plt.show()


#%%  一张图绘制两个曲线

from matplotlib import pyplot as plt
import numpy as np

a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,3,1,1]
b = [1,2,3,0,2,1,3,4,2,3,0,0,1,2,1,3,4,1,2,2]

x =[i for i in range(11,31)]
x_ticks =['{}岁'.format(i) for i in x]

# plt.plot(x,a,'r',x,b,'b') 可以一步到位

plt.plot(x,a,label ='自己',color ='r',linestyle ='--',linewidth='1')#设置颜色 线形 添加标签 
plt.plot(x,b,'g:',label ='同桌')#两种写法 注意位置！！！

#标注两条线！↑

plt.legend(loc =0)#将label贴到图像上 指定这个位置  调整label贴的位置  2是左上 0 是best




max_index=np.argmax(a)
min_index=np.argmin(a)

plt.xticks(x[::2],x_ticks[::2],rotation = 90)

plt.plot(max_index+11,max(a),'bp')#绘制出最大点所在位置




plt.show()

#-------------添加文本注释 标记出峰值 最小值















