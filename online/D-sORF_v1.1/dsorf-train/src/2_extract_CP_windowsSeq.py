import os
import sys
sys.path.append('./lib')
import re
import numpy as np
import matplotlib.pyplot as plt
from CP_features_extaction_module import *
from nMersDB import *


if len(sys.argv)==4:
    inputFileName = sys.argv[1]
    outputDir=sys.argv[2]
    startingPos=int(sys.argv[3])


##extract 54 nts windows for CP feature vector

bypassTisSignal=3*30 ##to be in frame left starting region
windowSize=54
maxnumOfWindowExtractedPerLine=5

outputFileName=outputDir+"CodingPotencialSequenceWindow.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
for aLine in inputFile:
    #print "\n"
    cols=aLine.strip().split("\t")
    seq=cols[1]
    windowsExtractionstartingPos=startingPos+bypassTisSignal
    if not len(seq)>(windowsExtractionstartingPos+windowSize): ##check the window end <transcript end else skip it
        continue
    netLength=len(seq)-windowsExtractionstartingPos
    modulo=netLength%windowSize
    maxNumOfWindows=(netLength-modulo)/windowSize
    if maxnumOfWindowExtractedPerLine>maxNumOfWindows:
        numWindows=maxNumOfWindows
    else:
        numWindows=maxnumOfWindowExtractedPerLine
    for windowCnt in range(0,numWindows):
        codingPotencialSeq=seq[windowsExtractionstartingPos+windowCnt*windowSize:windowsExtractionstartingPos+(windowCnt+1)*windowSize]
        #binaryStr=convertSeqToBinary(codingPotencialSeq)
        outputLine="\t".join([cols[0]+"|w"+str(windowCnt),codingPotencialSeq])
        outputFile.write(outputLine+"\n")
    
inputFile.close()
outputFile.close()
###################################################
##extract 54 nts windows for CP feature vector

bypassTisSignal=3*30 ##to be in frame left starting region
windowSize=54
maxnumOfWindowExtractedPerLine=1

outputFileName=outputDir+"CodingPotencialSequenceWindow54.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
for aLine in inputFile:
    #print "\n"
    cols=aLine.strip().split("\t")
    seq=cols[1]
    windowsExtractionstartingPos=startingPos+bypassTisSignal
    if not len(seq)>(windowsExtractionstartingPos+windowSize): ##check the window end <transcript end else skip it
        continue
    netLength=len(seq)-windowsExtractionstartingPos
    modulo=netLength%windowSize
    maxNumOfWindows=(netLength-modulo)/windowSize
    if maxnumOfWindowExtractedPerLine>maxNumOfWindows:
        numWindows=maxNumOfWindows
    else:
        numWindows=maxnumOfWindowExtractedPerLine
    for windowCnt in range(0,numWindows):
        codingPotencialSeq=seq[windowsExtractionstartingPos+windowCnt*windowSize:windowsExtractionstartingPos+(windowCnt+1)*windowSize]
        #binaryStr=convertSeqToBinary(codingPotencialSeq)
        outputLine="\t".join([cols[0]+"|w"+str(windowCnt),codingPotencialSeq])
        outputFile.write(outputLine+"\n")
    
inputFile.close()
outputFile.close()

###################################################


###################################################
##extract 99 nts windows for CP feature vector

bypassTisSignal=3*30 ##to be in frame left starting region
windowSize=99
maxnumOfWindowExtractedPerLine=1

outputFileName=outputDir+"CodingPotencialSequenceWindow99.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
for aLine in inputFile:
    #print "\n"
    cols=aLine.strip().split("\t")
    seq=cols[1]
    windowsExtractionstartingPos=startingPos+bypassTisSignal
    if not len(seq)>(windowsExtractionstartingPos+windowSize): ##check the window end <transcript end else skip it
        continue
    netLength=len(seq)-windowsExtractionstartingPos
    modulo=netLength%windowSize
    maxNumOfWindows=(netLength-modulo)/windowSize
    if maxnumOfWindowExtractedPerLine>maxNumOfWindows:
        numWindows=maxNumOfWindows
    else:
        numWindows=maxnumOfWindowExtractedPerLine
    for windowCnt in range(0,numWindows):
        codingPotencialSeq=seq[windowsExtractionstartingPos+windowCnt*windowSize:windowsExtractionstartingPos+(windowCnt+1)*windowSize]
        #binaryStr=convertSeqToBinary(codingPotencialSeq)
        outputLine="\t".join([cols[0]+"|w"+str(windowCnt),codingPotencialSeq])
        outputFile.write(outputLine+"\n")
    
inputFile.close()
outputFile.close()

###################################################
##extract 180 nts windows for CP feature vector

bypassTisSignal=3*30 ##to be in frame left starting region
windowSize=180
maxnumOfWindowExtractedPerLine=1

outputFileName=outputDir+"CodingPotencialSequenceWindow180.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
for aLine in inputFile:
    #print "\n"
    cols=aLine.strip().split("\t")
    seq=cols[1]
    windowsExtractionstartingPos=startingPos+bypassTisSignal
    if not len(seq)>(windowsExtractionstartingPos+windowSize): ##check the window end <transcript end else skip it
        continue
    netLength=len(seq)-windowsExtractionstartingPos
    modulo=netLength%windowSize
    maxNumOfWindows=(netLength-modulo)/windowSize
    if maxnumOfWindowExtractedPerLine>maxNumOfWindows:
        numWindows=maxNumOfWindows
    else:
        numWindows=maxnumOfWindowExtractedPerLine
    for windowCnt in range(0,numWindows):
        codingPotencialSeq=seq[windowsExtractionstartingPos+windowCnt*windowSize:windowsExtractionstartingPos+(windowCnt+1)*windowSize]
        #binaryStr=convertSeqToBinary(codingPotencialSeq)
        outputLine="\t".join([cols[0]+"|w"+str(windowCnt),codingPotencialSeq])
        outputFile.write(outputLine+"\n")
    
inputFile.close()
outputFile.close()

###################################################
##extract 50overlapping windows of 54 nts windows for CP feature vector

bypassTisSignal=3*30 ##to be in frame left starting region
windowSize=54
maxnumOfWindowExtractedPerLine=50
step=3

outputFileName=outputDir+"CodingPotencialSequenceWindow5054.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
lineCnt=0
for aLine in inputFile:
    #print aLine
    #print "\n"
    lineCnt+=1
    ###############################
    cols=aLine.strip().split("\t")
    seq=cols[1]
    #print seq
    #print seq[startingPos:]
    
    windowsExtractionstartingPos=startingPos+bypassTisSignal
    if not len(seq)>(windowsExtractionstartingPos+windowSize): ##check the window end <transcript end else skip it
        exit()
    netLength=len(seq)-windowsExtractionstartingPos
    modulo=netLength%step
    maxNumOfWindows=((netLength-modulo)-windowSize)/step+1
    if maxnumOfWindowExtractedPerLine>maxNumOfWindows:
        numWindows=maxNumOfWindows
    else:
        numWindows=maxnumOfWindowExtractedPerLine
        
    for windowCnt in range(0,numWindows):
        windowStart=windowsExtractionstartingPos+windowCnt*step
        codingPotencialSeq=seq[windowStart:windowStart+windowSize]
        outputLine="\t".join([cols[0]+"___"+str(lineCnt)+"___"+str(windowCnt+1),codingPotencialSeq])
        #print codingPotencialSeq
        outputFile.write(outputLine+"\n")
    

    
inputFile.close()
outputFile.close()