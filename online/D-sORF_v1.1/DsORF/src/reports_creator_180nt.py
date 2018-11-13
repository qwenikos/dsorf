import os
import sys


##PRIDEFile	SorfID	FixedMods	MzError	Charge	LorikeetId	Sequence	Rank	Precursormass	VariableMods	PeptideShakerConfidence

inputDirName="validation_negative_set_7_5_2018/"

workingDir="reports/neg/"


if len(sys.argv)==3:
    #print "argument are ok "
    inputDirName = sys.argv[1]
    workingDir=sys.argv[2]
    #sequenceToClassORFid=sys.argv[3]


command="mkdir -p "+workingDir
os.system(command)


attributeCPDict={}
attributeTISDict={}
attributeTIS9ntDict={}
posCPList=[]
negCPList=[]
posTIS12List=[]
negTIS12List=[]
posTIS9List=[]
negTIS9List=[]
generalDict={}

############################################

sorfFileDir=inputDirName
fileNamesListCP=[]
for root, dirs, files in os.walk(sorfFileDir):
    for filename in files:
        if filename[-len("COMB_results"):]=="COMB_results":
            # print root,files
            fileNamesListCP+=[os.path.join(root,filename)]
#print fileNamesListCP


############################################

fileNamesListTIS12=[]
for root, dirs, files in os.walk(sorfFileDir):
    for filename in files:
        if filename[-len("tis12.results"):]=="tis12.results":
            #print root,files
            fileNamesListTIS12+=[os.path.join(root,filename)]



############################################

fileNamesListTIS9=[]
for root, dirs, files in os.walk(sorfFileDir):
    for filename in files:
        if filename[-len("tis9.results"):]=="tis9.results":
            #print root,files
            #print os.path.join(root,filename)
            fileNamesListTIS9+=[os.path.join(root,filename)]


######################################
aDict={}
cpRresultsFileName="cp.results"
tis12RresultsFileName="tis12.results"
tis9RresultsFileName="tis9.results"
aDict[cpRresultsFileName]={}
aDict[tis12RresultsFileName]={}
aDict[tis9RresultsFileName]={}
##############################################
aFileList=fileNamesListCP
#print aFileList
akeyCol=8
for aFileName in aFileList:
    #print aFileName+"<<<<<"
    aFile=open(aFileName,"r")
    aDict[aFileName]={}
    for aLine in aFile:
        cols=aLine.rstrip().split("\t")
        aId=cols[akeyCol]  
        aDict[cpRresultsFileName][aId]=cols

    aFile.close()
###############################################
aFileList=fileNamesListTIS12
akeyCol=8
for aFileName in aFileList:

    aFile=open(aFileName,"r")
    aDict[aFileName]={}
    for aLine in aFile:
        cols=aLine.rstrip().split("\t")
        aId=cols[akeyCol]  
        aDict[tis12RresultsFileName][aId]=cols
        
    aFile.close()
##############################################
aFileList=fileNamesListTIS9
akeyCol=8
for aFileName in aFileList:

    aFile=open(aFileName,"r")
    aDict[aFileName]={}
    for aLine in aFile:
        cols=aLine.rstrip().split("\t")
        aId=cols[akeyCol]  
        aDict[tis9RresultsFileName][aId]=cols

    aFile.close()
##############################################

reportFileName=workingDir+"Report.csv"
reportFile=open(reportFileName,"w")
header="\t".join(["Id","Length","CPClass","CPscore","TIS9Classs","TIS9score","TIS12Class","TIS12score"])
reportFile.write(header+"\n")

posCPCnt=0
negCPCnt=0
posTISCnt=0
posTIS9Cnt=0
cntAll=0
for aKey in aDict[cpRresultsFileName]:

    if  (not aKey in aDict[tis12RresultsFileName]) or (not aKey in aDict[tis9RresultsFileName]):
        print "key not found",">>",aKey
        continue
    cntAll+=1
    #print [aKey]+aDict[cpRresultsFileName][aKey]+ aDict[tis12RresultsFileName][aKey]+aDict[tis9RresultsFileName][aKey]
    cpList=aDict[cpRresultsFileName][aKey]
    tis9List=aDict[tis9RresultsFileName][aKey]
    tis12List=aDict[tis12RresultsFileName][aKey]
    orfId=aKey
    orfLength=cpList[7]
    cpClass=int(cpList[0])
    cpScore=float(cpList[6])

    tis9Class=float(tis9List[0])
    tis9Score=float(tis9List[6])
    tis12Class=float(tis12List[0])
    tis12Score=float(tis12List[6])
    #aLineList=[aKey]+aDict[cpRresultsFileName][aKey]+ aDict[tis12RresultsFileName][aKey]+aDict[tis9RresultsFileName][aKey]
    aLineList=[orfId,orfLength,cpClass,cpScore,tis9Class,tis9Score,tis9Score,tis12Class,tis12Score]
    aLineSrt="\t".join(map(str,aLineList))+"\n"
    reportFile.write(aLineSrt)

reportFile.close()
##################################################

reportFileName=workingDir+"ReportThresholds.csv"
reportFile=open(reportFileName,"w")


reportFile.write("Thres"+"\t"+"cntAll"+"\t"+"posCPCnt"+"\t"+"posTISCnt"+"\t"+"posTIS9Cnt"+"\n")
for aThres in range(1,100,2):
    athreshold=aThres*1.0/100
    #print ">>",threshold
    posCPCnt=0
    negCPCnt=0
    posTISCnt=0
    posTIS9Cnt=0
    cntAll=0
      
    for aKey in aDict[cpRresultsFileName]:
    
        if  (not aKey in aDict[tis12RresultsFileName]) or (not aKey in aDict[tis9RresultsFileName]):
            print "key not found",">>",aKey
            continue
        cntAll+=1
        cpList=aDict[cpRresultsFileName][aKey]
        tis9List=aDict[tis12RresultsFileName][aKey]
        tis12List=aDict[tis9RresultsFileName][aKey]
        orfId=aKey
        orfLength=cpList[7]
        cpScore=float(cpList[6])
        #print ">>>",cpScore
        tis9Score=float(tis9List[6])
        tis12Score=float(tis12List[6])

        if cpScore>=athreshold:
            posCPCnt+=1
        if tis9Score>=athreshold:
            posTISCnt+=1
        if tis12Score>=athreshold:
            posTIS9Cnt+=1    

    reportFile.write(str(athreshold)+"\t"+str(cntAll)+"\t"+str(posCPCnt)+"\t"+str(posTISCnt)+"\t"+str(posTIS9Cnt)+"\n")
reportFile.close()
###############################################