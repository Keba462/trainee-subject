from django import forms
from trainee_subject.models.educational_questionaire import EducationalQuestionaire
from .forms_mixin import SubjectModelFormMixin


class EducationQuestionaireForm(SubjectModelFormMixin,forms.ModelForm):

    class Meta:
        model = EducationalQuestionaire
        fields = '__all__'