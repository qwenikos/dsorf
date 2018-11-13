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
    inputFileName2 = sys.argv[2]
    workingDir=sys.argv[3]
else:
    print "bad num of arguments"
    exit()

###########################

compute3mers=True
compute6mers=True
computeBinary=True
compute14Binary=True
computeAmino=True
computeNoATGBinary=True
computenMersFreq=True

###########################    

threeMersDict=convertListToDictOfInt(threeMersList) 
sixMersDict=convertListToDictOfInt(sixMersList)

frameNo=0

inputFile=open(inputFileName,"r")
inputFile2=open(inputFileName2,"r")


outputVectorCountsFileName_3=workingDir+"VectorizedCounts_3mers.tab"
outputVectorCountsFileName_6=workingDir+"VectorizedCounts_6mers.tab"

outputVectorFileName_3=workingDir+"Vectorized_3mers.tab"
outputVectorFileName_6=workingDir+"Vectorized_6mers.tab"
outputBinaryFileName=workingDir+"Binarize_12nts.tab"
outputBinaryNoATGFileName=workingDir+"BinarizeNoATG_9nts.tab"
outputBinary_14nt_FileName=workingDir+"Binarize_14nts.tab"
outputAminoVectorFileName=workingDir+"Vectorize_amino.tab"
outputFileName_3=workingDir+"3mers.tab"
outputFileName_6=workingDir+"6mers.tab"

if compute3mers==True:
    outputVectorFile_3=open(outputVectorFileName_3,"w")
    outputVectorCountsFile_3=open(outputVectorCountsFileName_3,"w")
if compute6mers==True:
    outputVectorFile_6=open(outputVectorFileName_6,"w")
    outputVectorCountsFile_6=open(outputVectorCountsFileName_6,"w")
if computeAmino==True:
    outputAminoVectorFile=open(outputAminoVectorFileName,"w")
if computeBinary==True:    
    outputBinaryFile=open(outputBinaryFileName,"w")
if compute14Binary==True:    
    outputBinary_14nt_File=open(outputBinary_14nt_FileName,"w")
if computeNoATGBinary==True:    
    outputBinaryNoATGFile=open(outputBinaryNoATGFileName,"w")
if computenMersFreq:
    outputFile_3=open(outputFileName_3,"w")  
    outputFile_6=open(outputFileName_6,"w")


   



ttt=0
for aLine in inputFile2:
    ttt+=1
    if ttt==200000000:
        break
    cols=aLine.rstrip().split("\t")
    #print cols
    seq=cols[1].rstrip()
    seq=seq[0:]
    #print seq
    seqLength=len(seq)
    
    ###binary 14 nt include start codon
    if compute14Binary==True:
        #print seq
        binaryStr=convertSeqToBinary(seq)
        binaryList=[]
        binaryList+=binaryStr
        binaryTabStr="\t".join(binaryList)
        outputBinary_14nt_File.write(binaryTabStr+"\n")
        
if compute14Binary==True:
    outputBinary_14nt_File.close()

inputFile2.close()  
###################################    
    #############################

ttt=0
for aLine in inputFile:
    ttt+=1
    if ttt==200000000:
        break
    cols=aLine.rstrip().split("\t")
    #print cols
    seq=cols[1].rstrip()
    seq=seq[0:]
    #print seq
    seqLength=len(seq)
    
    #############################
    ### 3mers
    if compute3mers==True:
        
        nmerLength=3
        seqTo3mersVector=[]
        threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
        threeMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in threeMers:
            threeMersDict[aItem]+=1
            
        for aItem in threeMersList:
            if aItem in threeMers:
                seqTo3mersVector+=[threeMersDict[aItem]]
                #seqTo3mersVector+=[1]
            else:
                seqTo3mersVector+=[0]
        #print seqTo3mersVector

        vectorLine="\t".join(map(str,seqTo3mersVector))
        outputVectorCountsFile_3.write(vectorLine+"\n")
        
        nomr_seqTo3mersVector=[float(x/18.0) for x in seqTo3mersVector]
        norm_vectorLine="\t".join(map(str,nomr_seqTo3mersVector))
        #outputVectorFile_3.write(norm_vectorLine+"\n")
        outputVectorFile_3.write(vectorLine+"\n")
###################################

    if compute6mers==True:
        nmerLength=6
        seqTo6mersVector=[]
        sixMersDict=convertListToDictOfInt(sixMersList)
        sixMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in sixMers:
            sixMersDict[aItem]+=1
    
            
        for aItem in sixMersList:
            if aItem in sixMers:
                seqTo6mersVector+=[sixMersDict[aItem]]
            else:
                seqTo6mersVector+=[0]
                
        vectorLine="\t".join(map(str,seqTo6mersVector))
        outputVectorCountsFile_6.write(vectorLine+"\n")
        
        nomr_seqTo6mersVector=[float(x/18.0) for x in seqTo6mersVector]
        norm_vectorLine="\t".join(map(str,nomr_seqTo6mersVector))
        #outputVectorFile_6.write(norm_vectorLine+"\n")
        outputVectorFile_6.write(vectorLine+"\n")
###################################        
    ###gencode amino
    if computeAmino==True:    
        nmerLength=3
        seqToAminoVectorDict={}
        seqToAminoVector=[]
        for i in range(1,23):
            seqToAminoVectorDict[i]=0
        threeMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in threeMers:
            aminoVectorPos=geneCodeDict[aItem]
            seqToAminoVectorDict[aminoVectorPos]+=1
            
        for j in sorted(seqToAminoVectorDict):
           seqToAminoVector+=[seqToAminoVectorDict[j]]
           #print j,seqToAminoVectorDict[j]
        #print   seqToAminoVector                  
        vectorLine="\t".join(map(str,seqToAminoVector))
        outputAminoVectorFile.write(vectorLine+"\n")
    
###################################
    ###binary 12 nt include start codon
    if computeBinary==True:
        binaryStr=convertSeqToBinary(seq)
        binaryList=[]
        binaryList+=binaryStr
        binaryTabStr="\t".join(binaryList)
        outputBinaryFile.write(binaryTabStr+"\n")
    
###################################
    ###binary 9nt nt exclude start codon
    if computeNoATGBinary==True:
        seqWithOutATG=seq[:7]+seq[-2:]
        binaryNoATGStr=convertSeqToBinary(seqWithOutATG)
        binaryNoATGList=[]
        binaryNoATGList+=binaryNoATGStr
        binaryNoATGTabStr="\t".join(binaryNoATGList)
        outputBinaryNoATGFile.write(binaryNoATGTabStr+"\n")
    ###binary 14nt nt exclude start codon

#####
#####
if computenMersFreq:
    cnt=0
    kmer3Idx=[]
    kmer3Count=[]
    for aKmer in threeMersList:
        kmer3Idx+=[cnt]
        kmer3Count+=[int(threeMersDict[aKmer])]
    
        cnt+=1
    ######
    cnt=0    
    kmer6Idx=[]
    kmer6Count=[]    
    for aKmer in sixMersList:
        kmer6Idx+=[cnt]
        kmer6Count+=[int(sixMersDict[aKmer])]
        cnt+=1
        
    ##################################################

    cnt=0
    for cnt in range(0,len(kmer3Idx)):
        outputFile_3.write(str(kmer3Idx[cnt])+"\t"+str(kmer3Count[cnt])+"\n")
    cnt=0    
    for cnt in range(0,len(kmer6Idx)):
        outputFile_6.write(str(kmer6Idx[cnt])+"\t"+str(kmer6Count[cnt])+"\n")


if computenMersFreq:
    outputFile_3.close()  
    outputFile_6.close()
if computeAmino==True:
    outputAminoVectorFile.close()
if compute6mers==True:
    outputVectorFile_6.close()
    outputVectorCountsFile_6.close()
if compute3mers==True:
    outputVectorFile_3.close()
    outputVectorCountsFile_3.close()
if computeBinary==True:    
    outputBinaryFile.close()
if compute14Binary==True:    
    outputBinary_14nt_File.close()
if computeNoATGBinary:
    outputBinaryNoATGFile.close()

inputFile.close()
#############################################################
