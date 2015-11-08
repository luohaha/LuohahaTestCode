# -*- coding:gb2312 -*-
__author__ = 'luoyixin'
from numpy import *

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        tmp = set(document)
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

##统计单词在词集合中出现的次数
def addWordInList(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        else:
            print "the word %s is not my word!" % word
    return returnVec

#贝叶斯分类器训练函数
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

#贝叶斯分类器
def classifyNB(vec, p0V, p1V, p):
    p1 = sum(vec * p1V) + log(p)
    p0 = sum(vec * p0V) + log(1-p)
    if p1 > p0:
        return 1
    else:
        return 0



def Main():
    listPost, listClass = loadDataSet()
    myWordList = createVocabList(listPost)
    trainMat = []
    for postInDoc in listPost:
        trainMat.append(addWordInList(myWordList, postInDoc))
    p0v, p1v, pab = trainNB0(trainMat, listClass)
    test = ['stupid', 'love']
    print classifyNB(addWordInList(myWordList, test), p0v, p1v, pab)
Main()