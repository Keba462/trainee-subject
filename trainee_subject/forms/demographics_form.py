from django import forms
from trainee_subject.models.demographics import Demographic
from .forms_mixin import SubjectModelFormMixin


class DemographicForm(SubjectModelFormMixin,forms.ModelForm):

    class Meta:
        model = Demographic
        fields = '__all__'