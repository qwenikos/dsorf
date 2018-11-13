baseOutputDir=final/

##positive_set_FileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/v8/createTrainingDataSets/proteinCoding_simulated_Datasets/POSITIVE/ensembl_proteinCoding_FLANK100_ofProteinCoding_withUNIPROTID_oneSeqPerId_train.fa"
#negative_set_FileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/v8/createTrainingDataSets/proteinCoding_simulated_Datasets/NEGATIVE/extract_negative_set_bypassing_2000_from_TSS/negativeSimORFSeq_train.fa"
positive_set_FileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/D-sORF_v1.0/DsORF-SimData/proteinCoding_simulated_Datasets/POSITIVE/ensembl_proteinCoding_FLANK100_ofProteinCoding_withUNIPROTID_oneSeqPerId_train.fa"
negative_set_FileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/D-sORF_v1.0/DsORF-SimData/proteinCoding_simulated_Datasets/NEGATIVE/create_NEGset_protCoding_15.000/negativeProtCoding_Flank-100.fa"
startingPos=100

python initialize_FeaturesExtraction.py $baseOutputDir $positive_set_FileName $negative_set_FileName $startingPos

limit=5000
retrain=Y  ##could be Y or N

python initialize_TIS_training.py $baseOutputDir $limit $retrain

python initialize_CP_training.py $baseOutputDir $limit $retrain

python initialize_comb_training.py $baseOutputDir $limit $retrain