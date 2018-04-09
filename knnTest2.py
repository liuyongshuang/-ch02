# -*- coding: utf-8 -*-
import kNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
reload(kNN)
zhFont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINWEI.TTF')
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')

# fig = plt.figure(figsize=(8, 5), dpi=80)
# ax = fig.add_subplot(111)
plt.figure(figsize=(8, 5), dpi=80)
ax = plt.subplot(111)
# 将三类数据分别取出来
# x轴代表飞行的里程数
# y轴代表玩视频游戏的百分比
type1_x = []
type1_y = []
type2_x = []
type2_y = []
type3_x = []
type3_y = []
print 'range(len(datingLabels)):'
print range(len(datingLabels))
for i in range(len(datingLabels)):
	if datingLabels[i] == 1: #不喜欢
		type1_x.append(datingDataMat[i][0])
		type1_y.append(datingDataMat[i][1])

	if datingLabels[i] == 2: #魅力一般
		type2_x.append(datingDataMat[i][0])
		type2_y.append(datingDataMat[i][1])

	if datingLabels[i] == 3: #极具魅力
		type3_x.append(datingDataMat[i][0])
		type3_y.append(datingDataMat[i][1])

#ax.scatter(datingDataMat[:,0], datingDataMat[:,1 ], 15.0*array(datingLabels), 15.0*array(datingLabels))
#plt.title("标题")
type1 = ax.scatter(type1_x, type1_y, s=20, c='red', marker='.')
type2 = ax.scatter(type2_x, type2_y, s=40, c='green', marker='*')
type3 = ax.scatter(type3_x, type3_y, s=50, c='blue', marker='+')
# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(datinglabels), 
# 			c=50 * numpy.array(datinglabels), marker='o', 
# 			label='test') #label='$test$'这个也可以显示图例

plt.xlabel(u'玩视频游戏所耗时间百分比',fontproperties = zhFont1)
plt.ylabel(u'每年获取的飞行常客里程数',fontproperties = zhFont1)
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2, prop=zhFont1)
plt.show()
