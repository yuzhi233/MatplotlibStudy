# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:41:38 2020

@author: zhoubo
"""

#绘制直方图  
#分清直方图和条形图区别！  这个老师讲的这节课有点乱


# 假设你获取了250部电影的时长(列表a中),
# 希望统计出这些电影时长的分布状态(比如时长为100分钟到120分钟电影的数量,出现的频率)
# 等信息,你应该如何呈现这些数据?

from matplotlib import pyplot as plt
import matplotlib


font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold',
        'size'   : '8'}
matplotlib.rc('font',**font)

#设置图像大小
plt.figure(figsize=(16,8),dpi = 80)


a=[131,  98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115,  99, 136, 126, 134,  95, 138, 117, 111,78, 132, 124, 113, 150, 110, 117,  86,  95, 144, 105, 126, 130,126, 130, 126, 116, 123, 106, 112, 138, 123,  86, 101,  99, 136,123, 117, 119, 105, 137, 123, 128, 125, 104, 109, 134, 125, 127,105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120, 114,105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134,156, 106, 117, 127, 144, 139, 139, 119, 140,  83, 110, 102,123,107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133,112, 114, 122, 109, 106, 123, 116, 131, 127, 115, 118, 112, 135,115, 146, 137, 116, 103, 144,  83, 123, 111, 110, 111, 100, 154,136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141,120, 117, 106, 149, 122, 122, 110, 118, 127, 121, 114, 125, 126,114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137,  92,121, 112, 146,  97, 137, 105,  98, 117, 112,  81,  97, 139, 113,134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110,105, 129, 137, 112, 120, 113, 133, 112,  83,  94, 146, 133, 101,131, 116, 111,  84, 137, 115, 122, 106, 144, 109, 123, 116, 111,111, 133, 150]


#分成20组 分的组数注意 组数=极差/组距
#plt.hist(a,20)

#计算组数 
d =3 #组距用d表示
num_bins =(max(a)-min(a))//d

#绘制直方图
plt.hist(a,num_bins,normed =True)

#这里需要注意 设置x轴刻度
plt.xticks(range(min(a),max(a)+d,d))#加组距是为了确保最大值能包含到  range步长的是d

#绘制网格

plt.grid()

plt.show()