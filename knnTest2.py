# -*- coding: utf-8 -*-
import kNN
#import numpy as np,np.array
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
reload(kNN)
zhFont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINWEI.TTF')
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
#print datingDataMat
#print datingLabels
fig = plt.figure()
#ax1 = fig.add_subplot(211)
#ax2 = fig.add_subplot(212)
ax = fig.add_subplot(111)
#colors = random.rand(1000)
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2], c='m', marker='+')
ax.scatter(datingDataMat[:,0], datingDataMat[:,1 ], 15.0*array(datingLabels), 15.0*array(datingLabels))
#plt.title("标题")
plt.xlabel(u"玩视频游戏所耗时间百分比",fontproperties = zhFont1)
plt.ylabel(u"每年获取的飞行常客里程数",fontproperties = zhFont1)

plt.show()
