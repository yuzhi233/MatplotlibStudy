# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:34:11 2020

@author: zhoubo
"""
import random
from matplotlib import pyplot as plt

#-------------------这里是设置字体----------------------
import matplotlib

font = {'family' : 'MicroSoft YaHei',
              'weight' : 'bold',
              'size'   : '10.'}
  
matplotlib.rc('font',**font)
#------------------------------------------------------

#设置y轴是2个小时（120分钟）的温度变化
y =  [random.randint(20, 30) for i in range(120)]

#设置x轴 size需要先和y轴一致
x = [i for i in range(120)]

#准备替换x轴刻度的列表x——
x_xticks = ['10点{}分'.format(i)for i in x if i<60 ]
x_xticks += ['11点{}分'.format(i-60) for i in x if i>=60]


plt.plot(x,y)

#替换原来的x轴刻度     这一步要在plot后设置
plt.xticks(x[::5],x_xticks[::5],rotation = 90)#列表分片太密集 步长取5

#设置x轴标，y轴标题
plt.xlabel('时间')
plt.ylabel('温度（C°）')

#设置标题
plt.title('2小时内温度变化')