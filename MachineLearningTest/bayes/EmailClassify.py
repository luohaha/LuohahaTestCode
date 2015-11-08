 # -*- coding:gb2312 -*-
__author__ = 'luoyixin'
from numpy import *
import re
import bayes

def textParse(str):
    listOfTokens = re.split(r'\W*', str)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []; classList=[]; fullText=[]
    for i in range(1, 26):
        wordList = textParse(open('./email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('./email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocalList = bayes.createVocabList(docList)
    trainingSet = range(50); testSet=[]
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[];trainClass=[];
    for docIndex in trainingSet:
        trainMat.append(bayes.addWordInList(vocalList, docList[docIndex]))
        trainClass.append(classList[docIndex])
    p0V,p1V,ps = bayes.trainNB0(array(trainMat), array(trainClass))
    errorCount = 0
    for doc in testSet:
        wordV = bayes.addWordInList(vocalList, docList[doc])
        if bayes.classifyNB(array(wordV), p0V, p1V, ps) != classList[doc]:
            errorCount+=1
    print 'err count is %d' % errorCount

spamTest()

