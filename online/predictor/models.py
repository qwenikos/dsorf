from django.db import models
# import  django.core.validators
# from django.core.validators import RegexValidator
# from django.core.validators import MaxValueValidator

# Create your models here.

class inputModel(models.Model):
    #from_email = forms.EmailField(required=True)
    emailFormItem=models.EmailField(max_length=70,blank=True)
    
    CHOICES=[('1','COMB'),('2','CP'),('3','TIS')]
    modelFormItem = models.CharField(choices=CHOICES,max_length=1,blank=False,default=None)
    
    SOME_CHOICES=[(True,'signalPeptideBypassFormItem'),(False,'NotsignalPeptideBypassFormItem')]
    bypassSignalPepFormItem = models.BooleanField(choices=SOME_CHOICES,default=False)

    # alphanumeric = RegexValidator(r'^[A-Z]*$', 'Only alphanumeric characters are allowed.')
    sORFSequenceFormItem = models.CharField(max_length=255)

    fileNameFormItem = models.FileField(upload_to='./%d/%m/%Y/')
    
    ATGStartingPosFormItem = models.IntegerField()
    
    simulateLength = models.IntegerField()