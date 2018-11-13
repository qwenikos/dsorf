
inputFileName="examples/test.fa"

mela_neg=/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/data/evaluationDatasets/phyloCSF_datasets/negative.fa
mela_pos=/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/data/evaluationDatasets/phyloCSF_datasets/positive.fa


inputFileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/v9/createTrainingDataSets/sORFS_simulated_DataSets/POSITIVE/Positive_sORFs_from_start_of_proteinSeq_70-300/sorfSimulatedWithOutPeptide.fa"
#inputFileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/v9/createTrainingDataSets/sORFS_simulated_DataSets/NEGATIVE/extract_negative_sorfs_set_bypassing_2000_from_TSS_210ntLength_15.000/negativeSORFSeq.fa"

#inputFileName="/home/perdikopn/Desktop/LINK_ECCB_PAPER/v9/createTrainingDataSets/sORFS_simulated_DataSets/NEGATIVE/extract_negative_sorfs_set_bypassing_2000_from_TSS_210ntLength_200.000/negativeSORFSeq.fa"
outputDir="7042018_phylocsf/"

#inputFileName=$mela_pos

numOfProcess=30
mode=2  ##1-combined 2=cp only 3= tis only
startingPos=103 
bypassSignalPeptide="N"  ##default=N
configFileName="conf/sORFconfig.cfg"
simulateLength=200 ##0 or "" for no simulation
python DsORF_init.py $inputFileName $outputDir $numOfProcess $mode $startingPos $bypassSignalPeptide $configFileName $simulateLength

inputDirName="output/7042018/"
workingDir=report/
#python reports_creator_180nt.py $inputDirName $workingDir
