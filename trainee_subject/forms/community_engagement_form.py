from django import forms
from trainee_subject.models.community_engagement import CommunityEngagement
from .forms_mixin import SubjectModelFormMixin
from trainee_validations.form_validators import CommunityEngagementValidationForm

class CommunityEngagementForm(SubjectModelFormMixin,forms.ModelForm):
    form_validator_cls = CommunityEngagementValidationForm

    class Meta:
        model = CommunityEngagement
        fields = '__all__'