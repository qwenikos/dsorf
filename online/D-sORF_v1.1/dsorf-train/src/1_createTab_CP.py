import os
import sys
sys.path.append('./lib')
import re
import numpy as np
import matplotlib.pyplot as plt
from CP_features_extaction_module import *
from nMersDB import *


if len(sys.argv)==3:
    faFileName = sys.argv[1]
    workingDir=sys.argv[2]
    
else:
    print "bad num of arguments"
    exit()
    

invalidDict={}
##################################################

###extract orfs
originalFaFile=open(faFileName,"r")

codingPotencialSeqMultiFaFileName=workingDir+"codingPotencialSeqMulti.fa"
codingPotencialSeqMultiFaFile=open(codingPotencialSeqMultiFaFileName,"w")

for aLine in originalFaFile:
    codingPotencialSeqMultiFaFile.write(aLine)

codingPotencialSeqMultiFaFile.close() 
originalFaFile.close()

#########################################################################
### convert multiline fa to single line   
codingPotencialSeqMultiFaFile=open(codingPotencialSeqMultiFaFileName,"r")
codingPotencialSeqSignleFaFileName=workingDir+"codingPotencialSeq.fa"
### to stop when stop codon found
codingPotencialSeqSignleFaFile=open(codingPotencialSeqSignleFaFileName,"w")
seq=""
for aLine in codingPotencialSeqMultiFaFile:
    aLine=aLine.rstrip().strip(" ")
    match = re.search('^>(.+)', aLine)
    if match:
        if not seq=='':
            codingPotencialSeqSignleFaFile.write(seq[:]+"\n")
        header=aLine
        codingPotencialSeqSignleFaFile.write(header+"\n")
        seq=""
    else:
        match = re.search('[ACTGactg]', aLine)
        if match:
            seq+=aLine
else: ##flush last seq at the end of the file
    codingPotencialSeqSignleFaFile.write(seq[:]+"\n")
codingPotencialSeqMultiFaFile.close()
codingPotencialSeqSignleFaFile.close()



sequenceFaFileName=workingDir+"codingPotencialSeq.fa"
sequenceTabFileName=workingDir+"codingPotencialSeq.tab"
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

sequenceTabValidFileName=workingDir+"codingPotencialSeq_valid.tab"
sequenceFaValidFileName=workingDir+"codingPotencialSeq_valid.fa"

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