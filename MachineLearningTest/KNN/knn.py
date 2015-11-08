from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1],[1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['a', 'a', 'b', 'b']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDis = sqDiffMat.sum(axis=1)
    distance = sqDis ** 0.5
    sortedLine = distance.argsort();
    classCount = {}
    for i in xrange(k):
        voteLable = labels[sortedLine[i]]
        classCount[voteLable] = classCount.get(voteLable, 0) + 1
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex