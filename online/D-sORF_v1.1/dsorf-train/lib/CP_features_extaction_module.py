### CREATE NMERRS SET

def make_kmers(k):
    kmersList=[]
    basesList=['A','C','T','G']
    if k==1:
        for i in range(0,4):
            kmersList+=[basesList[i]]
            print i
    if k==2:
        for i in range(0,4):
            for j in range(0,4):
                kmersList+=[basesList[i]+basesList[j]]
    if k==3:
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    kmersList+=[basesList[i]+basesList[j]+basesList[k]]        
    if k==4:
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    for l in range(0,4):
                        kmersList+=[basesList[i]+basesList[j]+basesList[k]+basesList[l]]
    if k==5:
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    for l in range(0,4):
                        for m in range(0,4):
                            kmersList+=[basesList[i]+basesList[j]+basesList[k]+basesList[l]+basesList[m]]
    if k==6:
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    for l in range(0,4):
                        for m in range(0,4):
                            for n in range(0,4):
                                kmersList+=[basesList[i]+basesList[j]+basesList[k]+basesList[l]+basesList[m]+basesList[n]]                 
    return kmersList

################################################################
def extractkmersFreqInFrameFromSeq(sequence,k,step,frame):
    ##frame must be 0 format in Frame 1,2 for other frames
    ##step  must be equal to k for no overlaping codons
    ##(seq,3,3,0) for not overlaping 3mers in frame

    kmerDict={}
    seqLength=len(sequence)
    nmerLength=k
    #print sequence
    for aBaseIdx in range(frame,seqLength,step):
        kMer=sequence[aBaseIdx:aBaseIdx+nmerLength]
        if not len(kMer)<k:
            if not kMer in kmerDict:
                kmerDict[kMer]=1
            else:
                kmerDict[kMer]+=1
    return kmerDict

################################################################

##extracting K-mers from sequence every step starting in frame (0,1,2)
def extractkmersInFrameFromSeq(sequence,k,step,frame):
    ##frame must be 0 format in Frame 1,2 for other frames
    ##step  must be equal to k for no overlaping codons
    ##(seq,3,3,0) for not overlaping 3mers in frame
    kmerList=[]
    seqLength=len(sequence)
    nmerLength=k
    #print sequence
    for aBaseIdx in range(frame,seqLength,step):
        kMer=sequence[aBaseIdx:aBaseIdx+nmerLength]
        if not len(kMer)<k:
            kmerList+=[kMer]
    return kmerList



################################################################
def convertListToDictOfInt(aList):
    aDict={}
    for aItem in aList:
        aDict[aItem]=0
    return aDict

################################################################
def convertListToDictOfList(aList):
    aDict={}
    for aItem in aList:
        aDict[aItem]=[]
    return aDict

################################################################   
def convertSeqToBinary(seq):
    codeDict={}
    outputBinaryStr=''
    codeDict['A']='1000'
    codeDict['C']='0100'
    codeDict['G']='0010'
    codeDict['T']='0001'
    codeDict['OTHER']='0000'
    for aBase in seq:
        if aBase in codeDict:
            outputBinaryStr+=codeDict[aBase]
        else:
            outputBinaryStr+=codeDict['OTHER']   
    return outputBinaryStr
        
################################################################
def rmSpecial(text):
    for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','|','$','\'',' ']:
        text = text.replace(ch,"_")
    return text
#######################
