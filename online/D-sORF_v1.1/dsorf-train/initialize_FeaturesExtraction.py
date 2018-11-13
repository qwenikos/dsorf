import os
import sys


currentPath=os.path.dirname(os.path.realpath(sys.argv[0]))+"/"

baseOutputDir="defaultOutput/"

if len(sys.argv)==5:
    #print "argument are ok "
    baseOutputDir           =sys.argv[1]
    positive_set_FileName   =sys.argv[2]
    negative_set_FileName   =sys.argv[3]
    startingPos             =sys.argv[4]
    
########a###################################

test=0
if test==1:
    positive_set_FileName   ="test.fa"  
    negative_set_FileName    ="test_no.fa"
 
    
###########################################
currentPath=currentPath+baseOutputDir

command="mkdir -p "+baseOutputDir
os.system(command)
cpDir=baseOutputDir+"cp/"
cpPosDir=cpDir+"positive/"
cpNegDir=cpDir+"negative/"
cpPosSeqDir=cpPosDir+"sequences/"
cpPosFeatDir=cpPosDir+"features/"
cpNegSeqDir=cpNegDir+"sequences/"
cpNegFeatDir=cpNegDir+"features/"
cpTrainingDir=cpDir+"training/"

command="mkdir -p "+cpPosSeqDir
os.system(command)
command="mkdir -p "+cpPosFeatDir
os.system(command)
command="mkdir -p "+cpNegSeqDir
os.system(command)
command="mkdir -p "+cpNegFeatDir
os.system(command)
command="mkdir -p "+cpTrainingDir
os.system(command)

tisDir=baseOutputDir+"tis/"
tisPosDir=tisDir+"positive/"
tisNegDir=tisDir+"negative/"
tisPosSeqDir=tisPosDir+"sequences/"
tisPosFeatDir=tisPosDir+"features/"
tisNegSeqDir=tisNegDir+"sequences/"
tisNegFeatDir=tisNegDir+"features/"
tisTrainingDir=tisDir+"training/"


command="mkdir -p "+tisPosSeqDir
os.system(command)
command="mkdir -p "+tisPosFeatDir
os.system(command)
command="mkdir -p "+tisNegSeqDir
os.system(command)
command="mkdir -p "+tisNegFeatDir
os.system(command)
command="mkdir -p "+tisTrainingDir
os.system(command)


combDir=baseOutputDir+"comb/"
combPosDir=combDir+"positive/"
combNegDir=combDir+"negative/"
combPosSeqDir=combPosDir+"sequences/"
combPosFeatDir=combPosDir+"features/"
combNegSeqDir=combNegDir+"sequences/"
combNegFeatDir=combNegDir+"features/"
combTrainingDir=combDir+"training/"


command="mkdir -p "+combPosSeqDir
os.system(command)
command="mkdir -p "+combPosFeatDir
os.system(command)
command="mkdir -p "+combNegSeqDir
os.system(command)
command="mkdir -p "+combNegFeatDir
os.system(command)
command="mkdir -p "+combTrainingDir
os.system(command)



##############################################

step1=True ## CP positive
step2=True ## CP negative
step3=True ##TIS positive
step4=True ##TIS negative
step5=True ##combined  180nt +TIS positive 54 nt +180 nt +TIS
step6=True ##combined  180nt +TIS negative

if step1:
    ############## positive CP ##################################

    inputFileName=positive_set_FileName
    outputDir=cpPosSeqDir
    command="python src/1_createTab_CP.py "+inputFileName+" " +outputDir
    print command
    os.system(command)
     
    inputFileName=cpPosSeqDir+"codingPotencialSeq_valid.tab"
    outputDir=cpPosFeatDir
    command="python src/2_extract_CP_windowsSeq.py "+inputFileName +" "+outputDir+" "+str(startingPos)
    print command
    os.system(command)
     
    inputFileName=cpPosFeatDir+"CodingPotencialSequenceWindow.tab"
    input54FileName=cpPosFeatDir+"CodingPotencialSequenceWindow54.tab"
    input100FileName=cpPosFeatDir+"CodingPotencialSequenceWindow99.tab" 
    input180FileName=cpPosFeatDir+"CodingPotencialSequenceWindow180.tab"
    input5054FileName=cpPosFeatDir+"CodingPotencialSequenceWindow5054.tab"
    outputDir=cpPosFeatDir
    command="python src/3_extract_CP_Features.py "+inputFileName+" "+input54FileName+" "+input100FileName+" "+input180FileName+" "+input5054FileName+" "+outputDir
    print command
    os.system(command)
    
    ###################################################

if step2:
    ############## negative CP ##################################

    inputFileName=negative_set_FileName
    outputDir=cpNegSeqDir
    command="python src/1_createTab_CP.py "+inputFileName+" " +outputDir
    print command
    os.system(command)
 
    inputFileName=cpNegSeqDir+"codingPotencialSeq_valid.tab"
    outputDir=cpNegFeatDir
    command="python src/2_extract_CP_windowsSeq.py "+inputFileName +" "+outputDir+" "+str(startingPos)
    print command
    os.system(command)
    
    inputFileName=cpNegFeatDir+"CodingPotencialSequenceWindow.tab"
    input54FileName=cpNegFeatDir+"CodingPotencialSequenceWindow54.tab"
    input100FileName=cpNegFeatDir+"CodingPotencialSequenceWindow99.tab"
    input180FileName=cpNegFeatDir+"CodingPotencialSequenceWindow180.tab"
    input5054FileName=cpNegFeatDir+"CodingPotencialSequenceWindow5054.tab"    

    outputDir=cpNegFeatDir
    command="python src/3_extract_CP_Features.py "+inputFileName+" "+input54FileName+" "+input100FileName+" "+input180FileName+" "+input5054FileName+" "+outputDir
    print command
    os.system(command)
    
    ################################################### 

if step3:
    ############## Positive  TIS ##################################
    startingPos=100

    inputFileName=positive_set_FileName
    outputDir=tisPosSeqDir
    command="python src/1_createTab_TIS.py "+inputFileName+" " +outputDir
    print command
    os.system(command)
 
    inputFileName=tisPosSeqDir+"tisSeq_valid.tab"
    outputDir=tisPosFeatDir
    command="python src/2_extract_TIS_windowsSeq.py "+inputFileName +" "+outputDir+" "+str(startingPos)
    print command
    os.system(command)
    
    inputFileName=tisPosFeatDir+"tisSequenceWindow.tab"
    inputFileName2=tisPosFeatDir+"tisSequenceWindow_14nt.tab"
    outputDir=tisPosFeatDir
    command="python src/3_extract_TIS_features.py "+inputFileName+" "+inputFileName2+" "  +outputDir
    print command
    os.system(command)

if step4:
    ############## negative  TIS ##################################

    inputFileName=negative_set_FileName
    outputDir=tisNegSeqDir
    command="python src/1_createTab_TIS.py "+inputFileName+" " +outputDir
    print command
    os.system(command)

    inputFileName=tisNegSeqDir+"tisSeq_valid.tab"
    outputDir=tisNegFeatDir
    command="python src/2_extract_TIS_windowsSeq.py "+inputFileName +" "+outputDir+" "+str(startingPos)
    print command
    os.system(command)
    
    inputFileName=tisNegFeatDir+"tisSequenceWindow.tab"
    inputFileName2=tisNegFeatDir+"tisSequenceWindow_14nt.tab"
    outputDir=tisNegFeatDir
    command="python src/3_extract_TIS_features.py "+inputFileName+" "+inputFileName2+" "  +outputDir
    print command
    os.system(command)
    
if step5:
    ############## Combined Positive 180nt ##################################
    inputTISFeatFileName=tisPosFeatDir+"BinarizeNoATG_9nts.tab"
    inputCPFeatFileName1=cpPosFeatDir+"Vectorized_54_3mers.tab"
    inputCPFeatFileName2=cpPosFeatDir+"Vectorized_99_3mers.tab"
    inputCPFeatFileName3=cpPosFeatDir+"Vectorized_180_3mers.tab"
    
    outputDir=combPosFeatDir
    command="python src/3_extract_Comb_Features.py "+inputTISFeatFileName+" "+inputCPFeatFileName1+" "+inputCPFeatFileName2+" "+inputCPFeatFileName3+" "  +outputDir
    print command
    os.system(command)

if step6:
    ############## Combined Negative 180nt ##################################
    inputTISFeatFileName=tisNegFeatDir+"BinarizeNoATG_9nts.tab"
    inputCPFeatFileName1=cpNegFeatDir+"Vectorized_54_3mers.tab"
    inputCPFeatFileName2=cpNegFeatDir+"Vectorized_99_3mers.tab"
    inputCPFeatFileName3=cpNegFeatDir+"Vectorized_180_3mers.tab"
    
    outputDir=combNegFeatDir
    command="python src/3_extract_Comb_Features.py "+inputTISFeatFileName+" "+inputCPFeatFileName1+" "+inputCPFeatFileName2+" "+inputCPFeatFileName3+" "  +outputDir
    print command
    os.system(command)
    


