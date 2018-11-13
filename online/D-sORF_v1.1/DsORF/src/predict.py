### sequence to be classified must be in bed format  with a  flanking region of 0 or more nts
import os
import sys
import sklearn
from sklearn.externals import joblib
import re

scriptDirectory =  os.path.abspath(os.path.dirname(__file__))+"/"
sys.path.append(scriptDirectory+"../")
#print (sys.path)
from  lib.CP_features_extaction_module  import *
from lib.nMersDB   import *
from lib.fn_module  import *

modelDirecory=scriptDirectory


######
##get from config
###read config file params
##### Read arguments ###########################
resultsFileName="default.results"
#startingPos=0
outputDir=""
combVector=""
cpVector=""
tisVector=""
modelCombFileName=""

if len(sys.argv)==11:
    #print "argument are ok "
    sequenceToClass = sys.argv[1]
    sequenceToClassLength=int(sys.argv[2])
    sequenceToClassORFid=sys.argv[3]
    startingPos=int(sys.argv[4])
    outputDir=sys.argv[5]
    signalPeptideBypaseMultiplier=int(sys.argv[6])
    mode=int(sys.argv[7])
    configFileName=sys.argv[8]
    resultsFileName=sys.argv[9]
    uid=sys.argv[10]
else:
    print ("------------------------\n-3_predict.py-\n-- No arguments Default values Used\n--\n------------------------\n")

##################################################
###### read config File
modelsFileName                  ={}
modelsFileName["COMB"]          ={}
modelsFileName["CP"]            ={}
modelsFileName["TIS"]           ={}
confDict=readConfigFile(configFileName)

dsorf_installation_directory=confDict["dsorf_installation_directory"]
if not (dsorf_installation_directory[-1:]=="/"):
    dsorf_installation_directory=dsorf_installation_directory+"/"
print ("D-sORF instalation >>> "+dsorf_installation_directory)

modelsFileName_COMB_54=confDict["modelsFileName_COMB_54"]
modelsFileName_COMB_99=confDict["modelsFileName_COMB_99"]
modelsFileName_COMB_180=confDict["modelsFileName_COMB_180"]
modelsFileName_CP_54=confDict["modelsFileName_CP_54"]
modelsFileName_CP_99=confDict["modelsFileName_CP_99"]
modelsFileName_CP_180=confDict["modelsFileName_CP_180"]
modelsFileName_TIS_9=confDict["modelsFileName_TIS_9"]
modelsFileName_TIS_12=confDict["modelsFileName_TIS_12"]

minLenLim=int(confDict["minLenLim"])
modelsFileName["COMB"]["54"]    =modelsFileName_COMB_54
modelsFileName["COMB"]["99"]   =modelsFileName_COMB_99
modelsFileName["COMB"]["180"]   =modelsFileName_COMB_180
modelsFileName["CP"]["54"]       =modelsFileName_CP_54
modelsFileName["CP"]["99"]     =modelsFileName_CP_99
modelsFileName["CP"]["180"]     =modelsFileName_CP_180
modelsFileName["TIS"]["9"]      =modelsFileName_TIS_9
modelsFileName["TIS"]["12"]     =modelsFileName_TIS_12
modelsFileName["TIS"]["54"]     = modelsFileName_TIS_9
modelsFileName["TIS"]["99"]    = modelsFileName_TIS_9
modelsFileName["TIS"]["180"]    =modelsFileName_TIS_9

##################################################

##model  and parameter selection

if   (sequenceToClassLength>startingPos+180)        : windowSize = 180  ##to see 
elif (sequenceToClassLength>startingPos+99)        : windowSize = 99
elif (sequenceToClassLength>startingPos+minLenLim)  : windowSize = 54

if   (sequenceToClassLength>startingPos+180)        : lengthClass = "180"
elif (sequenceToClassLength>startingPos+99)        : lengthClass = "99"
elif (sequenceToClassLength>startingPos+minLenLim)  : lengthClass = "54"

if   (mode==1)  : modelClass = "COMB"
elif (mode==2)  : modelClass = "CP"
elif (mode==3)  : modelClass = "TIS"


##model  and parameter selection
print ("Selected Model >>> ",lengthClass,modelClass)
selectedModelFileName=modelsFileName[modelClass][lengthClass]

##################################################
frameNo=0
step=3
bypassTisSignal=signalPeptideBypaseMultiplier*30 ##to be in frame left starting region




###################################

tisSeq=sequenceToClass[startingPos-7:startingPos+5]  #extract the TIS window
tisSeq=tisSeq[:7]+tisSeq[-2:] 

cpSeq=sequenceToClass[startingPos:startingPos+windowSize] #extract the CP window

process_3mers=True
if process_3mers:
    nmerLength=3
    seqTo3mersVector=[]
    threeMersDict=convertListToDictOfInt(threeMersList) ##initialize
    threeMers=extractkmersInFrameFromSeq(cpSeq,nmerLength,nmerLength,frameNo)
    for aItem in threeMers:
        threeMersDict[aItem]+=1
        
    for aItem in threeMersList:
        if aItem in threeMers:
            seqTo3mersVector+=[threeMersDict[aItem]]
            #seqTo3mersVector+=[1]
        else:
            seqTo3mersVector+=[0]
    threeMersVector="\t".join(map(str,seqTo3mersVector))

###################################
process_binary_NOATG=True
if process_binary_NOATG:
    binaryNoATGStr=convertSeqToBinary(tisSeq)
    binaryNoATGList=[]
    binaryNoATGList+=binaryNoATGStr
    binaryNoATGTabStr="\t".join(binaryNoATGList)

#############################################################


combVector="\t".join([binaryNoATGTabStr,threeMersVector]).split("\t")
cpVector=threeMersVector.split("\t")
tisVector=binaryNoATGTabStr.split("\t")

if   (mode==1)  : test_features=[combVector]
elif (mode==2)  : test_features=[cpVector]
elif (mode==3)  : test_features=[tisVector]


###### prediction

print ("selectedModelFileName",selectedModelFileName)

myNN = joblib.load(dsorf_installation_directory+selectedModelFileName)
predictions = myNN.predict(test_features)
decision=myNN.decision_function(test_features) ##propabilities 
decisionValue=decision[0]
print ("\n-----------------myNN.predict_proba-----START--------------------------\n")     
propa = myNN.predict_proba(test_features)
print ("\n-----------------myNN.predict_proba-----END--------------------------\n")  
prop1=float(propa[0][0])
prop2=float(propa[0][1])

##Reporting#########################################


aFile=open(outputDir+resultsFileName,"a")
aLine=[decisionValue,prop2,sequenceToClassLength,sequenceToClassORFid]

aFile.write("\t".join(map(str,aLine))+"\n")
aFile.close()



