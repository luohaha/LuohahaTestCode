# -*- coding: utf-8 -*-
__author__ = 'luoyixin'
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def calShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 1
        else:
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / numEntries
        shannonEnt -= p * log(p, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeactures = len(dataSet[0]) - 1
    baseEntropy = calShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeacture = -1
    for i in range(numFeactures):
        featList = [exa[i] for exa in dataSet]
        uniqueVal = set(featList)
        newEntropy = 0.0
        for value in uniqueVal:
            getDataSet = splitDataSet(dataSet, i, value)
            p = len(getDataSet) / float(len(dataSet))
            newEntropy += p * calShannonEnt(getDataSet) #获得加权后的香农熵
        #计算信息增益
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeacture = i
    return bestFeacture

#投票得出最终的结果
def majorClass(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedCount[0][0]

#创建树
def createTree(dataSet, labels):
    classList = [exa[-1] for exa in dataSet]
    if classList.count(classList[0]) == len(classList):
        #所有的类别都相同
        return classList[0]
    if len(dataSet[0]) == 1:
        #没有可以继续划分的类别了
        return majorClass(dataSet)
    bestFeast = chooseBestFeatureToSplit(dataSet)
    bestFeastLabel = labels[bestFeast]
    myTree = {bestFeastLabel:{}}
    #对于要划分的标签，获取其所有可能的取值
    feastValue = [exa[bestFeast] for exa in dataSet]
    uniqueValue = set(feastValue)
    del(labels[bestFeast])
    for value in uniqueValue:
        subLabels = labels[:]
        myTree[bestFeastLabel][value] = createTree(splitDataSet(dataSet, bestFeast, value), subLabels)
    return myTree
#分类器
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    feastIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if key == testVec[feastIndex]:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

myDat, labels = createDataSet()
print labels
newLaels = labels[:]
tree = createTree(myDat, newLaels)
print tree
print classify(tree, labels, [1,1])