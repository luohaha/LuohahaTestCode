from numpy import *
import os
import knn
def img2vector(filename):
    returnVect = zeros([1, 1024])
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():

    hwLabels = []
    trainListFiles = os.listdir('trainingDigits')
    m = len(trainListFiles)
    trainMat = zeros([m, 1024])
    for i in range(1, m):
        fileNameStr = trainListFiles[i]
        classNum = fileNameStr.split('.')[0].split('_')[0]
        hwLabels.append(classNum)
        trainMat[i-1,:] = img2vector('./trainingDigits/'+fileNameStr)
    testFileList = os.listdir('./testDigits')
    errorcount = 0.0
    mTest = len(testFileList)
    for i in range(1, mTest):
        fileNameStr = testFileList[i]
        classNum = fileNameStr.split('.')[0].split('_')[0]
        vectorForTest = img2vector('./testDigits/'+fileNameStr)
        classResult = knn.classify0(vectorForTest, trainMat, hwLabels, 3)
        print "result : "+classResult+" true : "+classNum
        if (classNum != classResult):
            errorcount += 1.0;
    print "all is : "+str(errorcount/mTest)

handwritingClassTest()