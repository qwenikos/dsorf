from django import forms
############ from model ###############################
from .models import inputModel

class inputForm(forms.ModelForm):
    class Meta:
        model=inputModel
        fields=("emailFormItem","modeFormItem","bypassSignalPepFormItem","inputTypeFormItem",
                "sORFSequenceFormItem","fileNameFormItem",
                "ATGStartingPosFormItem","simulateLength",)
        
        widgets={"modeFormItem":forms.Select(),
                 "inputTypeFormItem":forms.Select(),
            # "bypassSignalPepFormItem":forms.BooleanField(),
            "sORFSequenceFormItem":forms.Textarea(attrs={'rows':5}),     
        }
        
        # labels={"emailFormItem":"your email",
        #         "modeFormItem":"Select Model",
        #         "bypassSignalPepFormItem":'Bypass Signal Peptide',
        #         "sORFSequenceFormItem":'Give sORF Sequence',
        #         "fileNameFormItem":"or upload Filename",
        #         "ATGStartingPosFormItem":'ATG starting position',
        #         "simulateLength":'Give simulate length (optional)',
        # }
        
        labels={"emailFormItem":"",
                "modeFormItem":"",
                "bypassSignalPepFormItem":'',
                "inputTypeFormItem":'',
                "sORFSequenceFormItem":'',
                "fileNameFormItem":"",
                "ATGStartingPosFormItem":"",
                "simulateLength":"",
        }        
        
        help_texts = {"emailFormItem":"your email",
            "modeFormItem":"Select Mode",
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
        

