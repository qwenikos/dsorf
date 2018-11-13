import os
import sys
sys.path.append('./lib')
import re
import numpy as np
import matplotlib.pyplot as plt
from CP_features_extaction_module import *
from nMersDB import *


if len(sys.argv)==3:
    inputFileName = sys.argv[1]
    workingDir=sys.argv[2]
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
print "nikos"
invalidDict={}

##################################################

###extract orfs
originalFaFile=open(inputFileName,"r")

tisSeqMultiFaFileName=workingDir+"TisSeqMulti.fa"
codingPotencialSeqMultiFaFile=open(tisSeqMultiFaFileName,"w")

for aLine in originalFaFile:
    codingPotencialSeqMultiFaFile.write(aLine)
codingPotencialSeqMultiFaFile.close() 
originalFaFile.close()

#########################################################################
### convert multiline fa to single line   
tisSeqMultiFaFile=open(tisSeqMultiFaFileName,"r")
tisSeqSignleFaFileName=workingDir+"tisSeq.fa"
### to stop when stop codon found
tisSeqSignleFaFile=open(tisSeqSignleFaFileName,"w")
seq=""
for aLine in tisSeqMultiFaFile:
    aLine=aLine.rstrip().strip(" ")
    match = re.search('^>(.+)', aLine)
    if match:
        if not seq=='':
            tisSeqSignleFaFile.write(seq[:]+"\n")
        header=aLine
        tisSeqSignleFaFile.write(header+"\n")
        seq=""
    else:
        match = re.search('[ACTGactg]', aLine)
        if match:
            seq+=aLine
else: ##flush last seq at the end of the file
    tisSeqSignleFaFile.write(seq[:]+"\n")
tisSeqMultiFaFile.close()
tisSeqSignleFaFile.close()



sequenceFaFileName=workingDir+"tisSeq.fa"
sequenceTabFileName=workingDir+"tisSeq.tab"
sequenceFaFile=open(sequenceFaFileName,"r")
sequenceTabFile=open(sequenceTabFileName,"w")

for aLine in sequenceFaFile:
    aLine=aLine.strip()
    if  aLine[0]==">":  ##if( $line =~ />(.+)/ ){
        header=aLine
    else:
        sequenceTabFile.write(header+"\t"+aLine.upper()+"\n")
        if ("N" in aLine) or ("n" in aLine):
            invalidDict[header]=1

sequenceFaFile.close()
sequenceTabFile.close()

#######################################
##remove invalid entries

sequenceTabValidFileName=workingDir+"tisSeq_valid.tab"
sequenceFaValidFileName=workingDir+"tisSeq_valid.fa"

sequenceTabValidFile=open(sequenceTabValidFileName,"w")
sequenceFaValidFile=open(sequenceFaValidFileName,"w")
sequenceTabFile=open(sequenceTabFileName,"r")
#concatenate if multiline fa

for aLine in sequenceTabFile:
    cols=aLine.strip().split("\t")
    if not cols[0] in invalidDict:
        sequenceTabValidFile.write(aLine)
        sequenceFaValidFile.write(cols[0]+"\n"+cols[1]+"\n")
sequenceTabValidFile.close()
sequenceFaValidFile.close()


###################################################
