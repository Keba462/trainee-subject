from django import forms
from trainee_subject.models.subject_screening import SubjectScreening
#from trainee_validations.form_validators import ScreeningFormValidator

class SubjectScreeningForm(forms.ModelForm):

    #form_validator_cls = ScreeningFormValidator
    
    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectScreening
        fields = '__all__'