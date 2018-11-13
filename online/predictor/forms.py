from django import forms

from .models import inputModel

class inputForm(forms.ModelForm):
    class Meta:
        model=inputModel
        fields=("emailFormItem","modelFormItem","bypassSignalPepFormItem",
                "sORFSequenceFormItem","fileNameFormItem",
                "ATGStartingPosFormItem","simulateLength",)
        
    
import  django.core.validators
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator


class inputForm(forms.Form):
    
    emailFormItem = forms.EmailField(label='email', required=True)
    
    CHOICES=[('1','COMB'),('2','CP'),('3','TIS')]
    modelFormItem = forms.ChoiceField(label='Select Model',choices=CHOICES, widget=forms.Select,required=False)
    
    SOME_CHOICES=[(True,'signalPeptideBypassFormItem'),(False,'NotsignalPeptideBypassFormItem')]
    bypassSignalPepFormItem = forms.TypedChoiceField(choices=SOME_CHOICES,
                                                     label='Bypass Signal Peptide',
                                                     widget=forms.CheckboxInput(),
                                                     required=False)

    alphanumeric = RegexValidator(r'^[A-Z]*$', 'Only alphanumeric characters are allowed.')
    sORFSequenceFormItem = forms.CharField(label='Give sORF Sequence',
                                           widget=forms.Textarea(),
                                           required=False)

    fileNameFormItem = forms.FileField(label="or upload Filename",
                                       required=False
                                       )
    
    ATGStartingPosFormItem = forms.IntegerField(label='ATG starting position',
                                                min_value=1,
                                                required=True,
                                                validators=[MaxValueValidator(300)]
                                                )
    
    simulateLength = forms.IntegerField(label='Give simulate length (optional)',
                                        min_value=1,
                                        validators=[MaxValueValidator(300)],
                                        required=False
                                        )

