import os
import sys
sys.path.append('./lib')
import re
import numpy as np
import matplotlib.pyplot as plt
from CP_features_extaction_module import *
from nMersDB import *


if len(sys.argv)==6:
    inputTisFeatFileName = sys.argv[1]
    inputCpFeat54FileName = sys.argv[2]
    inputCpFeat99FileName = sys.argv[3]
    inputCpFeat180FileName = sys.argv[4]
    workingDir=sys.argv[5]
else:
    print "bad num of arguments"
    exit()

###########################
##combine CP 99nts  with TIS
tisVectorLineList=[]
cpVectorLineList=[]
inputTisFeatFile=open(inputTisFeatFileName,"r")
inputCpFeat99File=open(inputCpFeat99FileName,"r")
outputCombVector99FileName="Vector_Comb_CP_TIS_99.tab"
outputCombVector99File=open(workingDir+outputCombVector99FileName,"w")

limitOfSeqProcessed=1000000
tisVectorsCnt=0
for aLine in inputTisFeatFile:

    tisVectorLineList+=[aLine.rstrip()]
    tisVectorsCnt+=1

cpVectorsCnt=0
for aLine in inputCpFeat99File:
    cpVectorLineList+=[aLine.rstrip()]
    cpVectorsCnt+=1

minLineCnt=0
if (tisVectorsCnt<=cpVectorsCnt):
    minLineCnt=tisVectorsCnt
else:
    minLineCnt=cpVectorsCnt

for i in range(0,minLineCnt):
    #print i
    outputCombVector99File.write(tisVectorLineList[i]+"\t"+cpVectorLineList[i]+"\n")


inputCpFeat99File.close()
outputCombVector99File.close()

###########################
##combine CP 180nts  with TIS
tisVectorLineList=[]
cpVectorLineList=[]
inputTisFeatFile=open(inputTisFeatFileName,"r")
inputCpFeat180File=open(inputCpFeat180FileName,"r")
outputCombVector180FileName="Vector_Comb_CP_TIS_180.tab"
outputCombVector180File=open(workingDir+outputCombVector180FileName,"w")

limitOfSeqProcessed=1000000
tisVectorsCnt=0
for aLine in inputTisFeatFile:

    tisVectorLineList+=[aLine.rstrip()]
    tisVectorsCnt+=1

cpVectorsCnt=0
for aLine in inputCpFeat180File:
    cpVectorLineList+=[aLine.rstrip()]
    cpVectorsCnt+=1

minLineCnt=0
if (tisVectorsCnt<=cpVectorsCnt):
    minLineCnt=tisVectorsCnt
else:
    minLineCnt=cpVectorsCnt

for i in range(0,minLineCnt):
    #print i
    outputCombVector180File.write(tisVectorLineList[i]+"\t"+cpVectorLineList[i]+"\n")


inputCpFeat180File.close()
outputCombVector180File.close()

###########################
##combine CP 180nts  with TIS
tisVectorLineList=[]
cpVectorLineList=[]
inputTisFeatFile=open(inputTisFeatFileName,"r")
inputCpFeat54File=open(inputCpFeat54FileName,"r")
outputCombVector54FileName="Vector_Comb_CP_TIS_54.tab"
outputCombVector54File=open(workingDir+outputCombVector54FileName,"w")

limitOfSeqProcessed=1000000
tisVectorsCnt=0
for aLine in inputTisFeatFile:

    tisVectorLineList+=[aLine.rstrip()]
    tisVectorsCnt+=1

cpVectorsCnt=0
for aLine in inputCpFeat54File:
    cpVectorLineList+=[aLine.rstrip()]
    cpVectorsCnt+=1

minLineCnt=0
if (tisVectorsCnt<=cpVectorsCnt):
    minLineCnt=tisVectorsCnt
else:
    minLineCnt=cpVectorsCnt

for i in range(0,minLineCnt):
    #print i
    outputCombVector54File.write(tisVectorLineList[i]+"\t"+cpVectorLineList[i]+"\n")


inputCpFeat54File.close()
outputCombVector54File.close()

###########################


