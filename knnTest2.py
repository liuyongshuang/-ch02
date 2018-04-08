import kNN
reload(kNN)
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
print datingDataMat
print datingLabels
