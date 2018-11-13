import os
import sys

baseOutputDir="defaultOutput/"
currentPath=os.path.dirname(os.path.realpath(sys.argv[0]))+"/"

if len(sys.argv)==4:
    #print "argument are ok "
    baseOutputDir   =sys.argv[1]
    limit           =sys.argv[2]
    retrain         =sys.argv[3]


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
##############################################

step1=True  ##12nt train 
step2=True ##9nt train
step3=False ##6mers train
step4=False ##3mers train
step5=False ##amino train    
step6=True ##14 nt train   
###train

pos3mersFileName=tisPosFeatDir+"Vectorized_3mers.tab"
neg3mersFileName=tisNegFeatDir+"Vectorized_3mers.tab"

pos6mersFileName=tisPosFeatDir+"Vectorized_6mers.tab"
neg6mersFileName=tisNegFeatDir+"Vectorized_6mers.tab"

posBinarizedFileName=tisPosFeatDir+"Binarize_12nts.tab"
negBinarizedFileName=tisNegFeatDir+"Binarize_12nts.tab"

posBinarizedNoATGFileName=tisPosFeatDir+"BinarizeNoATG_9nts.tab"
negBinarizedNoATGFileName=tisNegFeatDir+"BinarizeNoATG_9nts.tab"

posBinarized14ntFileName=tisPosFeatDir+"Binarize_14nts.tab"
negBinarized14ntFileName=tisNegFeatDir+"Binarize_14nts.tab"

posAminoFileName=cpPosFeatDir+"Vectorize_amino.tab"
negAminoFileName=cpNegFeatDir+"Vectorize_amino.tab" 

if step1:
    ##################################################
    
    positiveFeaturesFileName=posBinarizedFileName
    negativeFeaturesFileName=negBinarizedFileName
    #retrain="Y"
    #limit=2000
    outputDir=tisTrainingDir
    
    modelFileName="tisModelBinarize12_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    ##################################################
if step2:    
    positiveFeaturesFileName=posBinarizedNoATGFileName
    negativeFeaturesFileName=negBinarizedNoATGFileName
    #retrain="Y"
    #limit=2000
    outputDir=tisTrainingDir
    
    modelFileName="tisModelBinarizeNoATG9_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)    
    
    ##################################################
if step3:    
    positiveFeaturesFileName=pos6mersFileName
    negativeFeaturesFileName=neg6mersFileName
    #retrain="Y"
    #limit=2000
    outputDir=tisTrainingDir
    
    modelFileName="tisModel6Mers_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    ##################################################
if step4:    
    positiveFeaturesFileName=pos3mersFileName
    negativeFeaturesFileName=neg3mersFileName
    #retrain="Y"
    #limit=2000
    outputDir=tisTrainingDir
    
    modelFileName="tisModel3Mers_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)     
    
    ##################################################
if step5:    
    positiveFeaturesFileName=posAminoFileName
    negativeFeaturesFileName=posAminoFileName
    retrain="Y"
    #limit=2000
    outputDir=tisTrainingDir
    
    modelFileName="cpModelAmino_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
  ##################################################  
if step6:    
    positiveFeaturesFileName=posBinarized14ntFileName
    negativeFeaturesFileName=negBinarized14ntFileName

    retrain="Y"
    #limit=2000
    outputDir=tisTrainingDir
    
    modelFileName="cpModelBinarize14nt_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)