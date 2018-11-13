from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import inputForm
import os


def input_form(request):
    #return render(request, 'input_form.html')
    if request.method == 'GET':
        form = inputForm()
        print("GET")
    else:
        form = inputForm(request.POST)
        print("POST")
        if form.is_valid():
            print ("-------------------------------------------------------")
            print ("A Valid form is submitted")
            print ("-------------------------------------------------------")
            model=form.cleaned_data['modelFormItem'] 
            bypassSignalPep=form.cleaned_data['bypassSignalPepFormItem']
            sORFSequence=form.cleaned_data['sORFSequenceFormItem']
            fileName=form.cleaned_data['fileNameFormItem']
            ATGStartingPos=form.cleaned_data['ATGStartingPosFormItem']
            
            sORFLength=len(sORFSequence)-int(ATGStartingPos)
            #print >>sys.stderr, 'Goodbye, cruel world!'
            print ("sORF sequence Length ---->"+str(sORFLength))
            
            inputType="0"

            if inputType=="0": ##sequence
                
                pathToDsORF="D-sORF_v1.1/DsORF/"
                outputDir="web"
                inputSeq=sORFSequence
                numOfProcess="1"
                mode=model
                startingPos=str(ATGStartingPos)
                if bypassSignalPep==False:
                    bypassSignalPeptide="0"
                else:
                    bypassSignalPeptide="1"
                    
                ##################
                uid="1002"
                ##################
                configFileName="default"
                simulateLength="0"
                print ("---------------------------")
                print ("inputType >>"+inputType)
                print ("pathToDsORF >>"+pathToDsORF)
                print ("outputDir >>"+outputDir)
                print ("inputSeq >>"+inputSeq)
                print ("numOfProcess >>"+numOfProcess)
                print ("mode >>"+mode)
                print ("startingPos >>"+startingPos)
                print ("bypassSignalPep >>"+bypassSignalPep)
                print ("bypassSignalPeptide >>"+bypassSignalPeptide)
                print ("configFileName >>"+configFileName)
                print ("simulateLength >>"+simulateLength)
                print ("---------------------------")
                print ("uid>>"+uid)
                resultsDir=pathToDsORF+"output"+"/"+outputDir+"/"+uid+"/"

                command= "python "+ pathToDsORF + "DsORF_init.py" +" "+ inputSeq + " " + outputDir+" "+numOfProcess+" "+mode+" " +startingPos+" "+bypassSignalPeptide +" "+configFileName+" "+simulateLength+" "+inputType+" "+uid
                
                print (command)
                print ("-----------DsORF_init.py---START-------------")
                os.system(command)
                print ("-----------DsORF_init.py---END-------------")
                
                #return HttpResponseRedirect('/results/')
                if   (int(mode)==1)  : modelClass = "COMB"
                elif (int(mode)==2)  : modelClass = "CP"
                elif (int(mode)==3)  : modelClass = "TIS"
                html=""
                resultsFileName=resultsDir+modelClass+'_stats'
                resultsFile=open(resultsFileName,"r")
                for aLine in resultsFile:
                    html+=aLine+"<br>"
                html='{% extends "base.html" %}<html><body><h1>DsOLF results</h1>'+html+'</html></body>'
                return HttpResponse(html)
            else:
                print("form is invalid")
                print(form.errors)


    return render(request, "input_form.html", {'form': form})
    #return HttpResponseRedirect('/thanks/')


def results(request):
    return render(request, 'results.html')

def index(request):
    return render(request, 'index.html')