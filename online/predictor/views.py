from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import inputForm
from collections import OrderedDict
import os

def save_uploaded_file(f,filename):
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
            print ("(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%)")
            print ("-------------------------------------------------------")
            print ("              A Valid form is submitted                ")
            print ("-------------------------------------------------------")
            email               =   form.cleaned_data['emailFormItem']
            mode                =   form.cleaned_data['modeFormItem'] 
            bypassSignalPep     =   form.cleaned_data['bypassSignalPepFormItem']
            inputTypeFormItem   =   form.cleaned_data['inputTypeFormItem']
            sORFSequence        =   form.cleaned_data['sORFSequenceFormItem']
            fileName            =   form.cleaned_data['fileNameFormItem']
            ATGStartingPos      =   form.cleaned_data['ATGStartingPosFormItem']
            
            if inputTypeFormItem==True:
                inputType='0'
            else:
                inputType='1'
                
            if inputTypeFormItem==True and sORFSequence=="":
                return JsonResponse({'error': True, 'message': 'Type=Text, Text=Empty'})
 
                
            if inputTypeFormItem==False and fileName==None:
                return JsonResponse({'error': True, 'message': 'Type=File, File=None'})
 
                
                
            if bypassSignalPep==False:
                bypassSignalPeptide="0"
            else:
                bypassSignalPeptide="1"
                
            if   (int(mode)==1)  : modelClass = "COMB"
            elif (int(mode)==2)  : modelClass = "CP"
            elif (int(mode)==3)  : modelClass = "TIS"            
            
            ### START database save ####
            form_initial_obj = form.save(commit=False)
            form_initial_obj.save()
            form.save()

             ##in db
            ### END database save  ###
            
            #return JsonResponse({'Stop': "Stop"})
            
            ### START save outside ###
            #uploaderFileName=request.FILES["fileNameFormItem"]
            # newFileName=email.replace("@","_at_")+"__"+str(uploaderFileName)
            # newFile=save_uploaded_file(request.FILES['fileNameFormItem'],newFileName)
            ### END save outside ###
            
            
            #return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
            


            
            #print >>sys.stderr, 'Goodbye, cruel world!'
            
            
            ##### START DsORF parameters #####
            pathToDsORF="D-sORF_v1.1/DsORF/"
            outputDir="web"
            inputSeq=sORFSequence
            numOfProcess="1"
            startingPos=str(ATGStartingPos)
            ##### END DsORF parameters #####
               
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
            print ("bypassSignalPep >>"+str(bypassSignalPep))
            print ("bypassSignalPeptide >>"+bypassSignalPeptide)
            print ("configFileName >>"+configFileName)
            print ("simulateLength >>"+simulateLength)
            print ("---------------------------")
            print ("uid>>"+uid)

            resultsDir=pathToDsORF+"output"+"/"+outputDir+"/"+uid+"/"


            if inputType=='0': ##sequence
                print ("continue with sequence")
                sORFLength=len(sORFSequence)-int(ATGStartingPos)
                print ("sORFLength",sORFLength)
                command= "python "+ pathToDsORF + "DsORF_init.py" +" "+ inputSeq + " " + outputDir+" "+numOfProcess+" "+mode+" " +startingPos+" "+bypassSignalPeptide +" "+configFileName+" "+simulateLength+" "+inputType+" "+uid
                print ("----+++------")
                print (command)
                print ("-----------DsORF_init.py---START-------------")
                os.system(command)
                print ("-----------DsORF_init.py---END-------------")
                
                #return HttpResponseRedirect('/results/')

                html=""
                ord_dict = OrderedDict()
                resultsFileName=resultsDir+modelClass+'_stats'
                resultsFile=open(resultsFileName,"r")
                lineNum=0
                for aLine in resultsFile:
                    html+=aLine+"<br>"
                    ord_dict[lineNum]=aLine
                    lineNum+=1
                resultFileURL="test.html" 
                #html='<body><h1>DsOLF results</h1>'+html+'</body>'

                return render(request, 'results.html',{'context': ord_dict,'resultFileURL':resultFileURL,'user_email':email})
                #return HttpResponse(html)
                #return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
                
            elif inputType=='1':
                savedFileName=form_initial_obj.fileNameFormItem.url
                if savedFileName[0]=="/":
                    savedFileName=savedFileName[1:]
                print(savedFileName)
                ### if file is uploader
                print ("continue with file")
                command= "python "+ pathToDsORF + "DsORF_init.py" +" "+ str(savedFileName) + " " + outputDir+" "+numOfProcess+" "+mode+" " +startingPos+" "+bypassSignalPeptide +" "+configFileName+" "+simulateLength+" "+inputType+" "+uid
                print ("----+++------")
                print (command)
                print ("-----------DsORF_init.py---START-------------")
                os.system(command)
                print ("-----------DsORF_init.py---END-------------")
                
                html=""
                ord_dict = OrderedDict()
                resultsFileName=resultsDir+modelClass+'_stats'
                resultsFile=open(resultsFileName,"r")
                lineNum=0
                for aLine in resultsFile:
                    html+=aLine+"<br>"
                    ord_dict[lineNum]=aLine
                    lineNum+=1
                resultFileURL="test.html" 
                #html='<body><h1>DsOLF results</h1>'+html+'</body>'

                return render(request, 'results.html',{'context': ord_dict,'resultFileURL':resultFileURL,'user_email':email})
                #return HttpResponse(html)
                #return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
                
        else:
            print("form is invalid")
            return JsonResponse({'error': True, 'errors': form.errors})
            print(form.errors)


    return render(request, "input_form.html", {'form': form})
    #return HttpResponseRedirect('/thanks/')


def results(request):
    return render(request, 'results.html',)

def index(request):
    return render(request, 'index.html')


# from django.shortcuts import render

# from .forms import inputForm

# def django_image_and_file_upload_ajax(request):
#     if request.method == 'POST':
#        form = inputForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
#        else:
#            return JsonResponse({'error': True, 'errors': form.errors})
#     else:
#         form = inputForm()
#         return render(request, 'django_image_upload_ajax.html', {'form': form})