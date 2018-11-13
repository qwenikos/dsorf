import os
import sys

baseOutputDir="defaultOutput/"
currentPath=os.path.dirname(os.path.realpath(sys.argv[0]))+"/"

if len(sys.argv)==4:
    #print "argument are ok "
    baseOutputDir   =sys.argv[1]
    limit           =sys.argv[2]
    retrain         =sys.argv[3]

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


step1=True  ##composite vector 64 of 180nt +9 nt binary TIS concensus
step2=True  ##composite vector 64 of 54nt +9 nt binary TIS concensusstep2=True
step3=True  ##composite vector 64 of 99nt +9 nt binary TIS concensus
###train
posCombVector180CpTis=combPosFeatDir+"Vector_Comb_CP_TIS_180.tab"
negCombVector180CpTis=combNegFeatDir+"Vector_Comb_CP_TIS_180.tab"

posCombVector54CpTis=combPosFeatDir+"Vector_Comb_CP_TIS_54.tab"
negCombVector54CpTis=combNegFeatDir+"Vector_Comb_CP_TIS_54.tab"

posCombVector99CpTis=combPosFeatDir+"Vector_Comb_CP_TIS_99.tab"
negCombVector99CpTis=combNegFeatDir+"Vector_Comb_CP_TIS_99.tab"




if step1:
    ##################################################
    print "--------------------***180nt**-----------------------------------------"
    positiveFeaturesFileName=posCombVector180CpTis
    negativeFeaturesFileName=negCombVector180CpTis
    #retrain="Y"
    #limit=2000
    outputDir=combTrainingDir
    
    modelFileName="combModelBin9_Win180_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
if step2:
    ##################################################
    print "--------------------***54nt**-----------------------------------------"
    positiveFeaturesFileName=posCombVector54CpTis
    negativeFeaturesFileName=negCombVector54CpTis
    #retrain="Y"
    #limit=2000
    outputDir=combTrainingDir
    
    modelFileName="combModelBin9_Win54_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)


if step3:
    ##################################################
    print "--------------------***99nt**-----------------------------------------"
    positiveFeaturesFileName=posCombVector99CpTis
    negativeFeaturesFileName=negCombVector99CpTis
    #retrain="Y"
    #limit=2000
    outputDir=combTrainingDir
    
    modelFileName="combModelBin9_Win99_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
##################################################