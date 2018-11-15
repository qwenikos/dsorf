from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import inputForm
import os

def handle_uploaded_file(f,filename):
    with open('./'+filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
def input_form(request):
    #return render(request, 'input_form.html')
    if request.method == 'GET':
        form = inputForm()
        print("GET")
    else:
        form = inputForm(request.POST, request.FILES)
        print("POST")
        if form.is_valid():
            print ("(%%%%%%%%%%%%%%%%%%%%%%%%%)")
            form.save() ##in db
            print (request.FILES["fileNameFormItem"])
            uploaderFileName=request.FILES["fileNameFormItem"]
            email=form.cleaned_data['emailFormItem'] 
            newFileName=email.replace("@","_at_")+"__"+str(uploaderFileName)
            print (newFileName)
            newFile=handle_uploaded_file(request.FILES['fileNameFormItem'],newFileName)
            
            
            print ("-------------------------------------------------------")
            print ("A Valid form is submitted")
            print ("-------------------------------------------------------")
            inputTypeFormItem=form.cleaned_data['inputTypeFormItem']
            print ("inputTypeFormItem",inputTypeFormItem)
            
            model=form.cleaned_data['modelFormItem'] 
            bypassSignalPep=form.cleaned_data['bypassSignalPepFormItem']
            sORFSequence=form.cleaned_data['sORFSequenceFormItem']
            fileName=form.cleaned_data['fileNameFormItem']
            ATGStartingPos=form.cleaned_data['ATGStartingPosFormItem']
            
            sORFLength=len(sORFSequence)-int(ATGStartingPos)
            #print >>sys.stderr, 'Goodbye, cruel world!'
            print ("sORF sequence Length ---->"+str(sORFLength))
            if inputTypeFormItem==True:
                print("--->Seq")
            if inputTypeFormItem==False:
                print("--->File")
                
                
            
   
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
            if inputTypeFormItem==True:
                inputType='0'
            else:
                inputType='1'

            if inputType=='0': ##sequence
                
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
                #return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
            else:
                ### if file is uploader
                print ("continue with file")
        else:
            print("form is invalid")
            return JsonResponse({'error': True, 'errors': form.errors})
            print(form.errors)


    return render(request, "input_form.html", {'form': form})
    #return HttpResponseRedirect('/thanks/')


def results(request):
    return render(request, 'results.html')

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render
from django.http import JsonResponse
from .forms import inputForm

def django_image_and_file_upload_ajax(request):
    if request.method == 'POST':
       form = inputForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = inputForm()
        return render(request, 'django_image_upload_ajax.html', {'form': form})