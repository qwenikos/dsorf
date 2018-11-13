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
    workingDir=sys.argv[2]
    startingPos=int(sys.argv[3])
else:
    print "bad num of arguments"
    exit()

    
###########################################################

refGenome="hg19"
if refGenome=="hg38":
    genome_file="GENOME/hg38.fa"
    chromSizes="GENOME/hg38.chrom.sizes"
    
if refGenome=="hg19":
    genome_file="/mnt/raid0/raid_common/Genomes/hg19/hg19.fa"
    chromSizes="/mnt/raid0/raid_common/Genomes/hg19/chrom.sizes"
    
###########################################################


##extract TIS feature vector

 ##pos of first letter of start coddon
#windowSize=12
windowStart=-7 ##fir
windowEndPos=+5



outputFileName=workingDir+"tisSequenceWindow.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
for aLine in inputFile:
    #print "\n"
    aLine=aLine.rstrip()
    cols=aLine.split("\t")
    seq=cols[1].rstrip()
    #print seq
    if not (len(seq)>=(startingPos+windowEndPos)and startingPos+windowStart>=0) : ##check the window end <transcript end else skip it
        continue
    tisSeq=seq[startingPos+windowStart:startingPos+windowEndPos]
    #binaryStr=convertSeqToBinary(codingPotencialSeq)
    outputLine="\t".join([cols[0],tisSeq])
    outputFile.write(outputLine+"\n")
inputFile.close()
outputFile.close()
#exit()###########################################################


##extract TIS feature vector

 ##pos of first letter of start coddon
#windowSize=14
windowStart=-7 ##fir
windowEndPos=+5



outputFileName=workingDir+"tisSequenceWindow_14nt.tab"
inputFile=open(inputFileName,"r")
outputFile=open(outputFileName,"w")
for aLine in inputFile:
    #print "\n"
    aLine=aLine.rstrip()
    cols=aLine.split("\t")
    seq=cols[1].rstrip()
    #print seq
    if not (len(seq)>=(startingPos+windowEndPos)and startingPos+windowStart>=0) : ##check the window end <transcript end else skip it
        continue
    tisSeq=seq[startingPos+windowStart:startingPos+windowEndPos]
    #binaryStr=convertSeqToBinary(codingPotencialSeq)
    outputLine="\t".join([cols[0],tisSeq])
    outputFile.write(outputLine+"\n")
inputFile.close()
outputFile.close()
#exit()