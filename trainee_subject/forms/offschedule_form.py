from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from trainee_subject.models.offschedule import OffSchedule



class OffScheduleForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = OffSchedule
        fields = '__all__'
