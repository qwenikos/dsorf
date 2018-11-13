import os
import sys
from multiprocessing import Pool
import subprocess

scriptDirectory =  os.path.abspath(os.path.dirname(__file__))+"/"
sys.path.append(scriptDirectory+"../")

#print (sys.path)
from  lib.CP_features_extaction_module  import *
from lib.nMersDB   import *
from lib.fn_module  import *
import re

##Default Values
simulateLength=""
numOfProcess=1
##end Default Values
### read arguments

if len(sys.argv)==14:
    #print "argument are ok "
    inputFileName = sys.argv[1]
    outputDir=sys.argv[2]
    signalPeptideBypaseMultiplier=sys.argv[3]
    startingPos=int(sys.argv[4])
    mode=int(sys.argv[5])
    numOfProcess=int(sys.argv[6])
    minLenLim=int(sys.argv[7])
    configFileName=sys.argv[8]
    inputFileName=sys.argv[9]
    simulateLength=sys.argv[10]
    uid=sys.argv[11]
    statsFileName=sys.argv[12]
    resultsFileName=sys.argv[13]
else:
    print ("------------------------\n-2_call_predict.py-\n-- No arguments Default values Used\n--\n------------------------\n")


### read arguments End

mp=True if numOfProcess>1 else False

idDir=os.path.basename(inputFileName)+"/"
print (outputDir)
#exit()
#outputDir=outputDir+idDir
#outputDir=outputDir+uid+"/"
#command="mkdir -p "+outputDir
#os.system(command)


####convert to tab format 
multiFaFile=open(inputFileName,"r")
singleFaFileName="singleLineFaFile.fa"
singleFaFile=open(outputDir+singleFaFileName,"w")
seq=""
for aLine in multiFaFile:
    aLine=aLine.rstrip().strip(" ")
    match = re.search('^>(.+)', aLine)
    if match:
        if not seq=='':
            singleFaFile.write(seq[:]+"\n")
        header=aLine
        singleFaFile.write(header+"\n")
        seq=""
    else:
        match = re.search('[ACTGactg]', aLine)
        if match:
            seq+=aLine
else: ##flush last seq at the end of the file
    singleFaFile.write(seq[:]+"\n")
multiFaFile.close()
singleFaFile.close()

sequenceFaFileName=outputDir+singleFaFileName
sequenceTabFileName=outputDir+"singleLineFaFile.tab"
sequenceFaFile=open(sequenceFaFileName,"r")
sequenceTabFile=open(sequenceTabFileName,"w")
invalidDict={}
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


######CP#######

inputFileName=sequenceTabFileName
#resultsFileName=os.path.basename(inputFileName)
print ("proccessing FileName >>> "+inputFileName)
sorfSeqList=[]
##for each sequence in file
aFile=open(inputFileName,"r")
for aLine in aFile:
    #print aLine
    aLine=aLine.rstrip().split("\t")
    #print aLine
    aSeq=aLine[1]
    
    if (not simulateLength=="") and (not simulateLength=="0"):
        aSeq=aSeq[:startingPos+int(simulateLength)]
        
    aSeqLength=len(aSeq)
    aSeqSorfId=rmSpecial(aLine[0])
    if aSeqLength<=startingPos+minLenLim:
        print  ("***EXCLUDE*** sORF with id "+aSeqSorfId+" < min length (startingPosOfOrf="+str(startingPos)+")")
        continue
    sorfSeqList+=[[aSeq,aSeqLength,aSeqSorfId]]
aFile.close()

# if   (mode==1)  : modelClass = "COMB"
# elif (mode==2)  : modelClass = "CP"
# elif (mode==3)  : modelClass = "TIS"
# 
# resultsFileName=modelClass+"_results"
# #outputDir=outputDir+resultsFileName+"/"
# statsFileName=modelClass+"_stats"
# command="mkdir -p "+outputDir
# os.system(command)
######


processing=True
if processing==True:
    
    command="rm -rf "+outputDir
    os.system(command)

    command="mkdir -p "+outputDir
    os.system(command)
    if  (mp==True):     
        def f(sorfSeqList):
            aSeq=sorfSeqList[0]
            aSeqLength=sorfSeqList[1]
            aSeqSorfId=sorfSeqList[2]
            print ("sORF Id >>>",aSeqSorfId)
            command="python "+scriptDirectory+"predict.py "+aSeq+" "+str(aSeqLength)+" "+aSeqSorfId+" "+str(startingPos)+" "+ outputDir+" "+str(signalPeptideBypaseMultiplier)+" "+str(mode)+" "+configFileName +" "+resultsFileName +" "+uid
            print (command)                                                                                                   
            os.system(command)
        p=Pool(numOfProcess) 
        p.map(f, sorfSeqList)
        
    else:
        for aItem in sorfSeqList:
            #print aItem
            aSeq=aItem[0]
            aSeqLength=aItem[1]
            aSeqSorfId=aItem[2]
            print (">>>",aSeqSorfId)
            #print aSeqSorfId
            command="python "+scriptDirectory+"predict.py "+aSeq+" "+str(aSeqLength)+" "+aSeqSorfId+" "+str(startingPos)+" "+ outputDir+" "+str(signalPeptideBypaseMultiplier)+" "+str(mode)+" "+configFileName +" "+resultsFileName+ " "+uid 
            print (command )                                                                                                     
            #os.system(command)
            print ("\n-----------------predict.py-----START--------------------------\n")
            sts = subprocess.Popen(command, shell=True).wait()
            print ("\n-----------------predict.py-----END--------------------------\n")
            
reporting=True      
if reporting==True:
    print ("\n--------------reporting---START --------------------------\n")
    aFile=open(outputDir+resultsFileName,"r")
    outFile=open(outputDir+statsFileName,"w")
    pos02Cnt=0
    pos05Cnt=0
    pos0875Cnt=0
    allCnt=0
    for aLine in aFile:
        allCnt+=1
        cols=aLine.rstrip().split("\t")
        aId=cols[3]
        aLength=int(cols[2])
        aPropa=float(cols[1])
        aDecFunc=float(cols[0])
        if aPropa>0.2:
            pos02Cnt+=1
            
        if aPropa>0.5:
            pos05Cnt+=1
            
        if aPropa>0.875:
            pos0875Cnt+=1    
        
    aFile.close()
    pos02CntPercent=truncate(float(pos02Cnt*1.0/allCnt*1.0),3)
    pos05CntPercent=truncate(float(pos05Cnt*1.0/allCnt*1.0),3)
    pos0875CntPercent=truncate(float(pos0875Cnt*1.0/allCnt*1.0),3)
    print ("allCnt",allCnt,"pos02Cnt",pos02Cnt,pos02CntPercent,"pos05Cnt",pos05Cnt,pos05CntPercent,"pos0875Cnt",pos0875Cnt,pos0875CntPercent)
    outFile.write("processed FileName"       + "\t" +inputFileName   +"\n" )
    outFile.write("Total num of sequences"   + "\t" + str(allCnt)    +"\n" )
    outFile.write("Threshold 0.2 Positives"  + "\t" + str(pos02Cnt)  +"\t" + "(" + str(pos02CntPercent)  + "%)" + "\n")
    outFile.write("Threshold 0.5 Positives"  + "\t" + str(pos05Cnt)  +"\t" + "(" + str(pos05CntPercent)  + "%)" + "\n")
    outFile.write("Threshold 0.875 Positives"+ "\t" + str(pos0875Cnt)+"\t" + "(" + str(pos0875CntPercent)+ "%)" + "\n")
    outFile.close()
    print ("\n--------------reporting---END --------------------------\n")

      