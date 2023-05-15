from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from trainee_subject.forms.sms_form import SMSForm

from trainee_subject.models.sms import SMS

from ..admin_site import trainee_subject_admin

from .model_admin_mixins import ModelAdminMixin


@admin.register(SMS, site=trainee_subject_admin)
class SMSAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SMSForm

    fieldsets = (
        (None, {
            'fields': ('subject_identifier',
                       'date_time_form_filled',
                       'next_ap_date',
                       'date_reminder_sent',
                       'sms_outcome'),
        }), audit_fieldset_tuple)

    radio_fields = {'sms_outcome': admin.VERTICAL}

    list_display = ('date_time_form_filled', 'next_ap_date',
                    'date_reminder_sent', 'sms_outcome')