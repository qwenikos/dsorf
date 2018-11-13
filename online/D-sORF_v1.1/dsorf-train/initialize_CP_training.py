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


    
pos3mersFileName=cpPosFeatDir+"Vectorized_3mers.tab"
neg3mersFileName=cpNegFeatDir+"Vectorized_3mers.tab"

pos3mersValFileName=cpPosFeatDir+"Vectorized_3mers.tab"
neg3mersValFileName=cpNegFeatDir+"Vectorized_3mers.tab"

pos6mersFileName=cpPosFeatDir+"Vectorized_6mers.tab"
neg6mersFileName=cpNegFeatDir+"Vectorized_6mers.tab"

posBinaryFileName=cpPosFeatDir+"binary_seq.tab"
negBinaryFileName=cpNegFeatDir+"binary_seq.tab"

posAminoFileName=cpPosFeatDir+"Vectorize_amino.tab"
negAminoFileName=cpNegFeatDir+"Vectorize_amino.tab"

pos3mers180FileName=cpPosFeatDir+"Vectorized_180_3mers.tab"
neg3mers180FileName=cpNegFeatDir+"Vectorized_180_3mers.tab"

pos3mers5054FileName=cpPosFeatDir+"Vectorized_5054_3mers.tab"
neg3mers5054FileName=cpNegFeatDir+"Vectorized_5054_3mers.tab"

pos3mers5054NormFileName=cpPosFeatDir+"Vectorized_5054_Norm_3mers.tab"
neg3mers5054NormFileName=cpNegFeatDir+"Vectorized_5054_Norm_3mers.tab"

pos3mers54FileName=cpPosFeatDir+"Vectorized_54_3mers.tab"
neg3mers54FileName=cpNegFeatDir+"Vectorized_54_3mers.tab"

pos3mers99FileName=cpPosFeatDir+"Vectorized_99_3mers.tab"
neg3mers99FileName=cpNegFeatDir+"Vectorized_99_3mers.tab"

#############################################################
    
step0=False  ##split data
step1=True  ##3mers train 
step2=False ##6mers train
step3=False ##amino train
step4=True ##3mers 180 nt
step5=False ##3mers 50 win of 54
step6=False ##3mers 50 win of 54 normalized
step7=True ##3mers 54 nt
step8=True ##3mers 99 nt


#############################################################
##split data to train and test Data
if step0:
    trainRatio=0.8
    positiveFeaturesFileName=pos3mersFileName
    negativeFeaturesFileName=neg3mersFileName
    outputDir=cpTrainingDir
    command="python src/6_splitData.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(trainRatio)
    print command
    #os.system(command)  
    
#############################################################
###train
if step1:
    print "*************\n********  3mers *********\n*****************"
    positiveFeaturesFileName=pos3mersFileName
    negativeFeaturesFileName=neg3mersFileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel3Mers_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    ####validation
    # print "###validation"
    # positiveFeaturesFileName=pos3mersValFileName
    # negativeFeaturesFileName=neg3mersValFileName
    # 
    # modelFileName="cpModel3Mers_"+str(limit)+".pkl"
    # command="python 8_validation.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    # print command
    # #os.system(command)
    
    
#############################################################

if step2:
    print "*************\n********  6mers *********\n*****************"
    positiveFeaturesFileName=pos6mersFileName
    negativeFeaturesFileName=neg6mersFileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel6Mers_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################
    
if step3:
    print "*************\n********  Aminomers *********\n*****************"
    positiveFeaturesFileName=posAminoFileName
    negativeFeaturesFileName=negAminoFileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModelAmino_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################
if step4:
    print "*************\n****** 3mers 180nt *******\n*****************"
    positiveFeaturesFileName=pos3mers180FileName

    negativeFeaturesFileName=neg3mers180FileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel3mers180_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################
if step5:
    print "*************\n********  5054 3mers *********\n*****************"
    positiveFeaturesFileName=pos3mers5054FileName
    negativeFeaturesFileName=neg3mers5054FileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel3mers5054_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################
    
if step6:
    print "*************\n*****  5054 norm mers *********\n*****************"
    positiveFeaturesFileName=pos3mers5054NormFileName
    negativeFeaturesFileName=neg3mers5054NormFileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel3mers5054norm_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################
if step7:
    print "*************\n****** 3mers 54nt *******\n*****************"
    positiveFeaturesFileName=pos3mers54FileName

    negativeFeaturesFileName=neg3mers54FileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel3mers54_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################
if step8:
    print "*************\n****** 3mers 99nt *******\n*****************"
    positiveFeaturesFileName=pos3mers99FileName

    negativeFeaturesFileName=neg3mers99FileName
    
    #retrain="Y"
    
    outputDir=cpTrainingDir
    
    modelFileName="cpModel3mers99_"+str(limit)+".pkl"
    command="python src/7_training.py "+" "+positiveFeaturesFileName+" "+negativeFeaturesFileName +" "+outputDir+" "+str(limit)+" "+retrain +" "+ modelFileName
    print command
    os.system(command)
    
    #################################################