from django import forms
############ from model ###############################
from .models import inputModel

class inputForm(forms.ModelForm):
    class Meta:
        model=inputModel
        fields=("emailFormItem","modelFormItem","bypassSignalPepFormItem","inputTypeFormItem",
                "sORFSequenceFormItem","fileNameFormItem",
                "ATGStartingPosFormItem","simulateLength",)
        
        widgets={"modelFormItem":forms.Select(),
                 "inputTypeFormItem":forms.Select(),
            # "bypassSignalPepFormItem":forms.BooleanField(),
            "sORFSequenceFormItem":forms.Textarea,     
        }
        
        # labels={"emailFormItem":"your email",
        #         "modelFormItem":"Select Model",
        #         "bypassSignalPepFormItem":'Bypass Signal Peptide',
        #         "sORFSequenceFormItem":'Give sORF Sequence',
        #         "fileNameFormItem":"or upload Filename",
        #         "ATGStartingPosFormItem":'ATG starting position',
        #         "simulateLength":'Give simulate length (optional)',
        # }
        
        labels={"emailFormItem":"",
                "modelFormItem":"",
                "bypassSignalPepFormItem":'',
                "inputTypeFormItem":'',
                "sORFSequenceFormItem":'',
                "fileNameFormItem":"",
                "ATGStartingPosFormItem":"",
                "simulateLength":"",
        }        
        
        help_texts = {"emailFormItem":"your email",
            "modelFormItem":"Select Model",
            "bypassSignalPepFormItem":'Bypass Signal Peptide',
            "inputTypeFormItem":'Select sequence TExt or File ',
            "sORFSequenceFormItem":'Give sORF Sequence',
            "fileNameFormItem":"or upload Filename",
            "ATGStartingPosFormItem":'ATG starting position',
            "simulateLength":'Give simulate length (optional)',
        }
        error_messages = {
            'emailFormItem': {
                'max_length': "This writer's name is too long.",
            },
        }
        
        
import  django.core.validators
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator

############with out model ###############################


# 
# class inputForm(forms.Form):
#     
#     emailFormItem = forms.EmailField(label='email', required=True)
#     
#     CHOICES=[('1','COMB'),('2','CP'),('3','TIS')]
#     modelFormItem = forms.ChoiceField(label='Select Model',choices=CHOICES, widget=forms.Select,required=False)
#     
#     SOME_CHOICES=[("1",'signalPeptideBypassFormItem'),("0",'NotsignalPeptideBypassFormItem')]
#     bypassSignalPepFormItem = forms.TypedChoiceField(choices=SOME_CHOICES,
#                                                      label='Bypass Signal Peptide',
#                                                      widget=forms.CheckboxInput(),
#                                                      required=False)
# 
#     alphanumeric = RegexValidator(r'^[A-Z]*$', 'Only alphanumeric characters are allowed.')
#     sORFSequenceFormItem = forms.CharField(label='Give sORF Sequence',
#                                            widget=forms.Textarea(),
#                                            required=False)
# 
#     fileNameFormItem = forms.FileField(label="or upload Filename",
#                                        required=False
#                                        )
#     
#     ATGStartingPosFormItem = forms.IntegerField(label='ATG starting position',
#                                                 min_value=1,
#                                                 required=True,
#                                                 validators=[MaxValueValidator(300)]
#                                                 )
#     
#     simulateLength = forms.IntegerField(label='Give simulate length (optional)',
#                                         min_value=1,
#                                         validators=[MaxValueValidator(300)],
#                                         required=False
#                                         )

