from django.db import models
# import  django.core.validators
# from django.core.validators import RegexValidator
# from django.core.validators import MaxValueValidator

# Create your models here.

class inputModel(models.Model):
    #from_email = forms.EmailField(required=True)
    emailFormItem=models.EmailField(max_length=70,blank=True)
    
    CHOICES=[('1','COMB'),('2','CP'),('3','TIS')]
    modeFormItem = models.CharField(choices=CHOICES,max_length=1,blank=False,default=None)
    
    SOME_CHOICES=[(True,'Yes'),(False,'No')]
    bypassSignalPepFormItem = models.BooleanField(choices=SOME_CHOICES,default=False)
    
    SEQ_FILE_CHOISES=[(True,'Sequence'),(False,'File')]
    inputTypeFormItem=models.BooleanField(choices=SEQ_FILE_CHOISES,default=True)

    # alphanumeric = RegexValidator(r'^[A-Z]*$', 'Only alphanumeric characters are allowed.')
    sORFSequenceFormItem = models.CharField(max_length=255 ,blank=True)

    fileNameFormItem = models.FileField(upload_to='./%d/%m/%Y/', blank=True)
    
    ATGStartingPosFormItem = models.IntegerField()
    
    simulateLength = models.IntegerField(blank=True,default=0)