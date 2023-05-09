from django import forms
from trainee_subject.models.educational_questionaire import EducationalQuestionaire
from .forms_mixin import SubjectModelFormMixin
from trainee_validations.form_validators import EducationQuestionaireValidationForm

class EducationQuestionaireForm(SubjectModelFormMixin,forms.ModelForm):

    form_validator_cls = EducationQuestionaireValidationForm

    class Meta:
        model = EducationalQuestionaire
        fields = '__all__'