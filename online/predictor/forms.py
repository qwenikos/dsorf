from django import forms
import  django.core.validators
from django.core.validators import RegexValidator
class inputForm(forms.Form):
    #from_email = forms.EmailField(required=True)
    
    CHOICES=[('1','COMB'),('2','CP'),('3','TIS')]
    modelFormItem = forms.ChoiceField(label='Select Model',choices=CHOICES, widget=forms.Select,required=False)
    
    SOME_CHOICES=[(True,'signalPeptideBypassFormItem'),(False,'NotsignalPeptideBypassFormItem')]
    #signalPepFormItem = forms.ChoiceField(label='Bypass Signal Peptide ', widget=forms.CheckboxInput,required=False)
    bypassSignalPepFormItem = forms.TypedChoiceField(choices=SOME_CHOICES,label='Bypass Signal Peptide', widget=forms.CheckboxInput(),required=False)

    alphanumeric = RegexValidator(r'^[A-Z]*$', 'Only alphanumeric characters are allowed.')
    #sORFSequenceFormItem = forms.CharField(label='Give sORF Sequence',widget=forms.Textarea, required=True,validators=[alphanumeric])
    sORFSequenceFormItem = forms.CharField(label='Give sORF Sequence',widget=forms.Textarea(attrs={'rows': 5, 'cols': 80}), required=True)

    fileNameFormItem = forms.FileField(label="or upload Filename",required=False)
    
    ATGStartingPosFormItem = forms.IntegerField(label='ATG starting position',min_value=1,required=True)
    simulateLength = forms.IntegerField(label='Give simulate length (optional))',min_value=1,required=False)


