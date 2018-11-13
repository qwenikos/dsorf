import os
import sys
from  lib.CP_features_extaction_module import *
from lib.nMersDB import *
from lib.fn_module import *
import subprocess

print ("sys.version",sys.version)
print ("---------------------------")

baseOutputDir="defaultOutput/"
currentPath=os.path.dirname(os.path.realpath(sys.argv[0]))+"/"

###DefaultValues Start
scriptDirectory =  os.path.abspath(os.path.dirname(__file__))+"/"
outputDir=""
defaultConfigFileName=scriptDirectory+"conf/sORFconfig.cfg"
##print (configFileName)

numOfProcess=1 ##for parallel processing of module
mode=1
signalPeptideBypase=0 ##select 0 to not bypassing signlal peptide zone 1)bypass

simulateLength=""
###DefaultValues End

if len(sys.argv)==9:
    #print "argument are ok "
    inputData   =sys.argv[1]
    outputDir       =sys.argv[2]
    numOfProcess    =sys.argv[3]
    mode            =sys.argv[4]
    startingPos     =sys.argv[5]
    signalPeptideBypase=sys.argv[6]
    configFileName=sys.argv[7]
    input_type      =sys.argv[8] ##0 for seq 1 for filename
    
if len(sys.argv)==11:
    #print "argument are ok "
    inputData   =sys.argv[1]
    outputDir       =sys.argv[2]
    numOfProcess    =sys.argv[3]
    mode            =sys.argv[4]
    startingPos     =sys.argv[5]
    signalPeptideBypase=sys.argv[6]
    configFileName=sys.argv[7]
    simulateLength=sys.argv[8]
    input_type      =sys.argv[9] ##0 for seq 1 for file name
    uid=sys.argv[10]
    
if input_type=="0":
    tempFileName="tempInputFile.fa"
    tempFile=open(tempFileName,"w")
    tempFile.write(">tempSorfId\n")
    tempFile.write(inputData+"\n")
    tempFile.close()
    inputData="tempInputFile.fa"

if configFileName=="default":
    configFileName=defaultConfigFileName

if int(startingPos)<7 and (not (int(mode)==2)):
    print ("cannot continue with this mode due to upstream region length. Select  mode 2 (Coding Combisition only)")
    exit()

if signalPeptideBypase=="0":
    signalPeptideBypaseMultiplier=0
elif signalPeptideBypase=="1":
    signalPeptideBypaseMultiplier=3

print ("signalPeptideBypaseMultiplier >>> ",signalPeptideBypaseMultiplier)


###read config file params
print ("configFileName >>> ",configFileName)
confDict=readConfigFile(configFileName)
outputStartingDir=confDict["outputStartingDir"]
outputStartingDir=currentPath+outputStartingDir
minLenLim=confDict["minLenLim"]
#########################



if (not outputStartingDir=="") and  (not outputStartingDir[-1:]=="/"):
    outputStartingDir=outputStartingDir+"/"
    
if (not outputDir=="") and (not outputDir[-1:]=="/"):
    outputDir=outputDir+"/"

outputDir=outputStartingDir+outputDir+uid+"/"
print ("outputDir >>> ",outputDir)

command="mkdir -p "+outputDir
os.system(command)

#########################
#modelClass=""
if   (int(mode)==1)  : modelClass = "COMB"
elif (int(mode)==2)  : modelClass = "CP"
elif (int(mode)==3)  : modelClass = "TIS"

resultsFileName=modelClass+"_results"
#outputDir=outputDir+resultsFileName+"/"
statsFileName=modelClass+"_stats"
######



command="python "+scriptDirectory+"src/call_predict.py "+inputData+" "+outputDir+" "+str(signalPeptideBypaseMultiplier)+" "+str(startingPos)+" "+str(mode)+" "+str(numOfProcess)+" "+minLenLim+" "+configFileName +" "+inputData+" "+ simulateLength+" "+uid+" "+statsFileName+" "+resultsFileName
print ("command >>>>>"+command)


#os.system(command
print ("\n-----------------call_predict.py-----START--------------------------\n")
sts = subprocess.Popen(command, shell=True).wait()
print ("\n-----------------call_predict.py-----END--------------------------\n")

outFile=open(outputDir+statsFileName,"r")
for aLine in outFile:
    print (aLine)
    
print ("-----------------DsORF_init.py-----END--------------------------")



