from django import forms
from trainee_subject.models.community_engagement import CommunityEngagement
from .forms_mixin import SubjectModelFormMixin


class CommunityEngagementForm(SubjectModelFormMixin,forms.ModelForm):

    class Meta:
        model = CommunityEngagement
        fields = '__all__'