from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import knn
def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(arrayOlines)
    returnMat = zeros([numberOfLines, 3])
    classLabelVector = []
    index = 0
    for line in arrayOlines:
        line = line.strip()
        listFromLines = line.split('\t')
        returnMat[index, :] = listFromLines[0:3]
        if cmp(listFromLines[-1], 'largeDoses') == 0:
            classLabelVector.append(int(3))
        elif cmp(listFromLines[-1], 'smallDoses') == 0:
            classLabelVector.append(int(2))
        elif cmp(listFromLines[-1], 'didntLike') == 0:
            classLabelVector.append(int(1))
        else:
            print 'err'
        index += 1
    return returnMat, classLabelVector
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = ones(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
def datingClassTest():
    rating = 0.1
    datingDataMat, labels = file2matrix("./datingTestSet.txt")
    normDataSet, ranges, minVals = autoNorm(datingDataMat)
    m = normDataSet.shape[0]
    testNum = int(m * rating)
    err = 0.0
    for i in range(testNum):
        index = knn.classify0(normDataSet[i, :], normDataSet, labels, 3)
        print "predict:"+str(index)+" real:"+str(labels[i])
        if (index != labels[i]):
            err += 1.0
    print str(err)+":"+str(m)
def begin():
    resultList = ['not at all', 'a litte like', 'like very much']
    a = float(raw_input("percent"))
    b = float(raw_input("miles"))
    c = float(raw_input("liter"))
    inX = array([a, b, c])
    datingDataMat, labels = file2matrix("./datingTestSet.txt")
    normData, range, min = autoNorm(datingDataMat)
    classRes = knn.classify0((inX-min)/range, normData, labels, 3)
    return resultList[classRes-1]
#datingDataMat, labels = file2matrix("./datingTestSet.txt")
#normDataSet, ranges, minVals = autoNorm(datingDataMat)
#print normDataSet
res = begin()
print res