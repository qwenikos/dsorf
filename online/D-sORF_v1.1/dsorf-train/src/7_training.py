import sklearn
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn import svm
import numpy as np
import sys


if len(sys.argv)==7:
    print "argument are ok "
    postitiveSetFileName = sys.argv[1]
    negativeSetFileName=sys.argv[2]
    outputDir=sys.argv[3]
    limit=int(sys.argv[4])
    retrain=sys.argv[5]
    modelFileName=sys.argv[6]
else:
    print "error in args"
    
postitiveSetFile=open(postitiveSetFileName,"r")
negativeSetFile=open(negativeSetFileName,"r")
postitiveFeaturesList=[]
negativeFeaturesList=[]
postitiveLabelsList=[]
negativeLabelsList=[]

cnt=0

for aLine in postitiveSetFile:
    cnt+=1
    #print aLine
    cols=aLine.rstrip().split("\t")
    postitiveFeaturesList+=[cols]
    postitiveLabelsList+=[1]
    if cnt>=limit:
        break
    
cnt=0
for aLine in negativeSetFile:
    cnt+=1
    #print aLine
    cols=aLine.rstrip().split("\t")
    negativeFeaturesList+=[cols]
    negativeLabelsList+=[-1]
    if cnt>=limit:
        break
    
postitiveLabelsList=map(int,postitiveLabelsList)   
negativeLabelsList=map(int,negativeLabelsList)


allFeaturesList=postitiveFeaturesList+negativeFeaturesList
allLabelsList=postitiveLabelsList+negativeLabelsList
##print allLabelsList
features, labels = sklearn.utils.shuffle(allFeaturesList, allLabelsList)
print "shuffling"
features, labels = sklearn.utils.shuffle(features, labels)
print "splitting"
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3)
    
if retrain=="Y":
    ###Training SVM
    myNN= svm.SVC(cache_size=30000,kernel='poly',probability=True)
    print "fitting"
    myNN.fit(train_features, train_labels)
    print "save model to disk",outputDir+modelFileName
    joblib.dump(myNN, outputDir+modelFileName)
else:
    myNN = joblib.load(outputDir+modelFileName) 


print "predict"
predictions = myNN.predict(test_features)
#decisions=myNN.decision_function(test_features)
# print  predictions
# print decisions
# print test_labels
# exit()
print "metrics"
svmAccuracy = sklearn.metrics.accuracy_score(test_labels, predictions)
print "==================="
print svmAccuracy
print "==================="
confusion_matrix = sklearn.metrics.confusion_matrix(test_labels, predictions)
true_negative, false_positive, false_negative, true_positive = confusion_matrix.ravel()
print(true_positive,false_positive,true_negative,false_negative)
classification_report = sklearn.metrics.classification_report(test_labels, predictions)
print("classification_report:")
print(classification_report)
