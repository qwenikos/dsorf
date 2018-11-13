import sys
sys.path.append('./lib')
from CP_features_extaction_module import *
from nMersDB import *

#print len(sys.argv)
if len(sys.argv)==7:
    print " args ok"
    inputFileName = sys.argv[1]
    input54FileName = sys.argv[2]
    input99FileName = sys.argv[3]
    input180FileName = sys.argv[4]
    input5054FileName = sys.argv[5]
    workingDir=sys.argv[6]
    
###########################

compute3mers=True
computeBinary=False
compute6mers=False
computeAmino=False
computenMersFreq=False
compute_54_3mers=True
compute_99_3mers=True
compute_180_3mers=True
compute_5054_3mers=True

###########################

threeMersDict=convertListToDictOfInt(threeMersList) 
sixMersDict=convertListToDictOfInt(sixMersList)
threeMersAllSeqDict=convertListToDictOfInt(threeMersList)
sixMersAllSeqDict=convertListToDictOfInt(sixMersList)

frameNo=0

inputFile=open(inputFileName,"r")
input54File=open(input54FileName,"r")
input99File=open(input99FileName,"r")
input180File=open(input180FileName,"r")
input5054File=open(input5054FileName,"r")
outputVectorCountsFileName_3=workingDir+"VectorizedCounts_3mers.tab"
outputVectorCountsFileName_6=workingDir+"VectorizedCounts_6mers.tab"

outputVectorFileName_3=workingDir+"Vectorized_3mers.tab"
outputVectorFileName_6=workingDir+"Vectorized_6mers.tab"
outputBinaryFileName=workingDir+"binary_seq.tab"
outputAminoVectorFileName=workingDir+"Vectorize_amino.tab"
outputFileName_3=workingDir+"3mers.tab"
outputFileName_6=workingDir+"6mers.tab"

output180VectorFileName_3=workingDir+"Vectorized_180_3mers.tab"
output54VectorFileName_3=workingDir+"Vectorized_54_3mers.tab"
output99VectorFileName_3=workingDir+"Vectorized_99_3mers.tab"
output5054VectorFileName_3=workingDir+"Vectorized_5054_3mers.tab"
output5054NormVectorFileName_3=workingDir+"Vectorized_5054_Norm_3mers.tab"

if computenMersFreq:
    outputFile_3=open(outputFileName_3,"w")  
    outputFile_6=open(outputFileName_6,"w")
if computeAmino==True:
    outputAminoVectorFile=open(outputAminoVectorFileName,"w")
    
if compute6mers==True:
    outputVectorFile_6=open(outputVectorFileName_6,"w")
    outputVectorCountsFile_6=open(outputVectorCountsFileName_6,"w")
if compute3mers==True:
    outputVectorFile_3=open(outputVectorFileName_3,"w")
    outputVectorCountsFile_3=open(outputVectorCountsFileName_3,"w")
if computeBinary==True:    
    outputBinaryFile=open(outputBinaryFileName,"w")
    
if compute_54_3mers==True:
    output54VectorFile_3=open(output54VectorFileName_3,"w")

if compute_99_3mers==True:
    output99VectorFile_3=open(output99VectorFileName_3,"w")
    
if compute_180_3mers==True:
    output180VectorFile_3=open(output180VectorFileName_3,"w")

if compute_5054_3mers==True:
    output5054VectorFile_3=open(output5054VectorFileName_3,"w")
    output5054NormVectorFile_3=open(output5054NormVectorFileName_3,"w")

limitOfSeqProcessed=1000000
seqCnt=0
for aLine in inputFile:
    
    seqCnt+=1
    if seqCnt>=limitOfSeqProcessed:
        break

    cols=aLine.split("\t")
    seq=cols[1].rstrip()
    seqLength=len(seq)
    
    ########################################################
    ### 3mers
    
    if compute3mers==True:
        nmerLength=3
        seqTo3mersVector=[]
        threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
        threeMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in threeMers:
            threeMersDict[aItem]+=1
            threeMersAllSeqDict[aItem]+=1
    
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
    ########################################################
    #binary
 
    if computeBinary==True:    
        binaryStr=convertSeqToBinary(seq)
        binaryList=[]
        binaryList+=binaryStr
        binaryTabStr="\t".join(binaryList)
        outputBinaryFile.write(binaryTabStr+"\n")

    ########################################################
    ### 6mers

    if compute6mers==True:
        nmerLength=6
        seqTo6mersVector=[]
        sixMersDict=convertListToDictOfInt(sixMersList)
        sixMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in sixMers:
            sixMersDict[aItem]+=1
            sixMersAllSeqDict[aItem]+=1
            
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
    ########################################################
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

########################################################
##proceess 99 nt window
if compute_99_3mers:
    limitOfSeqProcessed=1000000
    seqCnt=0
    for aLine in input99File:
        
        seqCnt+=1
        if seqCnt>=limitOfSeqProcessed:
            break
    
        cols=aLine.split("\t")
        seq=cols[1].rstrip()
        seqLength=len(seq)
        
        ########################################################
        ### 3mers
        
        nmerLength=3
        seqTo3mersVector=[]
        threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
        threeMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in threeMers:
            threeMersDict[aItem]+=1
            threeMersAllSeqDict[aItem]+=1
    
        for aItem in threeMersList:
            if aItem in threeMers:
                seqTo3mersVector+=[threeMersDict[aItem]]
                #seqTo3mersVector+=[1]
            else:
                seqTo3mersVector+=[0]
        #print seqTo3mersVector
        
        vectorLine="\t".join(map(str,seqTo3mersVector))
        #outputVectorCountsFile_3.write(vectorLine+"\n")
        
        nomr_seqTo3mersVector=[float(x/18.0) for x in seqTo3mersVector]
        norm_vectorLine="\t".join(map(str,nomr_seqTo3mersVector))
        #outputVectorFile_3.write(norm_vectorLine+"\n")
        output99VectorFile_3.write(vectorLine+"\n")
########################################################


###################################
##proceess 180 nt window
if compute_180_3mers:
    limitOfSeqProcessed=1000000
    seqCnt=0
    for aLine in input180File:
        
        seqCnt+=1
        if seqCnt>=limitOfSeqProcessed:
            break
    
        cols=aLine.split("\t")
        seq=cols[1].rstrip()
        seqLength=len(seq)
        
        ########################################################
        ### 3mers
        
        nmerLength=3
        seqTo3mersVector=[]
        threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
        threeMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in threeMers:
            threeMersDict[aItem]+=1
            threeMersAllSeqDict[aItem]+=1
    
        for aItem in threeMersList:
            if aItem in threeMers:
                seqTo3mersVector+=[threeMersDict[aItem]]
                #seqTo3mersVector+=[1]
            else:
                seqTo3mersVector+=[0]
        #print seqTo3mersVector
        
        vectorLine="\t".join(map(str,seqTo3mersVector))
        #outputVectorCountsFile_3.write(vectorLine+"\n")
        
        nomr_seqTo3mersVector=[float(x/18.0) for x in seqTo3mersVector]
        norm_vectorLine="\t".join(map(str,nomr_seqTo3mersVector))
        #outputVectorFile_3.write(norm_vectorLine+"\n")
        output180VectorFile_3.write(vectorLine+"\n")
########################################################

###################################
##proceess 54 nt window
if compute_54_3mers:
    limitOfSeqProcessed=1000000
    seqCnt=0
    for aLine in input54File:
        
        seqCnt+=1
        if seqCnt>=limitOfSeqProcessed:
            break
    
        cols=aLine.split("\t")
        seq=cols[1].rstrip()
        seqLength=len(seq)
        
        ########################################################
        ### 3mers
        
        nmerLength=3
        seqTo3mersVector=[]
        threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
        threeMers=extractkmersInFrameFromSeq(seq,nmerLength,nmerLength,frameNo)
        for aItem in threeMers:
            threeMersDict[aItem]+=1
            threeMersAllSeqDict[aItem]+=1
    
        for aItem in threeMersList:
            if aItem in threeMers:
                seqTo3mersVector+=[threeMersDict[aItem]]
                #seqTo3mersVector+=[1]
            else:
                seqTo3mersVector+=[0]
        #print seqTo3mersVector
        
        vectorLine="\t".join(map(str,seqTo3mersVector))
        #outputVectorCountsFile_3.write(vectorLine+"\n")
        
        nomr_seqTo3mersVector=[float(x/18.0) for x in seqTo3mersVector]
        norm_vectorLine="\t".join(map(str,nomr_seqTo3mersVector))
        #outputVectorFile_3.write(norm_vectorLine+"\n")
        output54VectorFile_3.write(vectorLine+"\n")

###########################################################    
if compute_5054_3mers:
    limitOfSeqProcessed=1000000
    seqCnt=0
    nmerLength=3
    aDict={}
    for aLine in input5054File:
        seqCnt+=1
        if seqCnt>=limitOfSeqProcessed:
            break
        cols=aLine.split("\t")
        headerCols=cols[0].split("___")
        lineId=headerCols[1]
        seqId=headerCols[2]
    
        sequence=cols[1].rstrip()
        seqLength=len(sequence)
        
        if not lineId in aDict:
            aDict[lineId]=[]
        aDict[lineId]+=[sequence]

    for aLineList in aDict:
        line3mersVector=[0]*64
        line3mersNormVector=[0]*64

        
        sequenceInLineCnt=0
        for aSeq in aDict[aLineList]:
            threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
            #print aSeq
            sequenceInLineCnt+=1
            sequence3mersVector=[]
            sequence3mersNormVector=[]
            
            threeMers=extractkmersInFrameFromSeq(aSeq,nmerLength,nmerLength,frameNo)
            #print threeMers
            for aItem in threeMers:
                threeMersDict[aItem]+=1
            
            for aItem in threeMersList:
                if aItem in threeMers:
                    sequence3mersVector+=[threeMersDict[aItem]]
                    sequence3mersNormVector+=[int(threeMersDict[aItem])*1.0/18*1.0]
                    #seqTo3mersVector+=[1]
                else:
                    sequence3mersVector+=[0]
                    sequence3mersNormVector+=[0]
            #print sequence3mersVector
            #print sequence3mersNormVector
        #print len(sequence3mersVector)
            for aPos in range(0,len(sequence3mersVector) ):
                #print sequence3mersVector
                line3mersVector[aPos]=line3mersVector[aPos]+sequence3mersVector[aPos]
                line3mersNormVector[aPos]=line3mersNormVector[aPos]+sequence3mersNormVector[aPos]
        #print line3mersVector
        for aPos in range(0,len(line3mersNormVector) ):
            line3mersNormVector[aPos]=line3mersNormVector[aPos]*1.0/sequenceInLineCnt*1.0
        #print line3mersNormVector
        vectorLine="\t".join(map(str,line3mersVector))
        normVectorLine="\t".join(map(str,line3mersNormVector))
        output5054VectorFile_3.write(vectorLine)
        output5054NormVectorFile_3.write(normVectorLine)
 
        ########################################################
        
    
###################################


if computenMersFreq:

    cnt=0
    kmer3Idx=[]
    kmer3Count=[]
    for aKmer in threeMersList:
        kmer3Idx+=[cnt]
        kmer3Count+=[int(threeMersAllSeqDict[aKmer])]
        cnt+=1
    
    cnt=0    
    kmer6Idx=[]
    kmer6Count=[]    
    for aKmer in sixMersList:
        kmer6Idx+=[cnt]
        kmer6Count+=[int(sixMersAllSeqDict[aKmer])]
        cnt+=1

    cnt=0
    for cnt in range(0,len(kmer3Idx)):
        outputFile_3.write(str(kmer3Idx[cnt])+"\t"+str(kmer3Count[cnt])+"\n")
    cnt=0    
    for cnt in range(0,len(kmer6Idx)):
        outputFile_6.write(str(kmer6Idx[cnt])+"\t"+str(kmer6Count[cnt])+"\n")
        
#####################################
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
if compute_99_3mers:
    output99VectorFile_3.close() 
if compute_180_3mers:
    output180VectorFile_3.close() 
if compute_5054_3mers:
    output5054VectorFile_3.close()
    output5054NormVectorFile_3.close()
if compute_54_3mers:    
    output54VectorFile_3.close()
inputFile.close()




########################################