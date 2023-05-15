from django.contrib import admin
from django.conf import settings
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites import ModelAdminSiteMixin
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_model_admin import ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, \
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin, \
    ModelAdminRedirectOnDeleteMixin, FormAsJSONModelAdminMixin
from edc_visit_tracking.modeladmin_mixins import (
    CrfModelAdminMixin as VisitTrackingCrfModelAdminMixin)
from edc_metadata import NextFormGetter


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):
    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter
    extra_context_models = None


class CrfModelAdminMixin(VisitTrackingCrfModelAdminMixin,
                         ModelAdminMixin,
                         FieldsetsModelAdminMixin,
                         FormAsJSONModelAdminMixin,
                         admin.ModelAdmin):
    post_url_on_delete_name = 'study_subject:subject_dashboard_url'
    instructions = (
        'Please complete the questions below. Required questions are in bold. '
        'When all required questions are complete click SAVE. '
        'Based on your responses, additional questions may be '
        'required or some answers may need to be corrected.')
    

    def post_url_on_delete_kwargs(self, request, obj):
            return dict(
                subject_identifier=obj.subject_identifier,
                appointment=str(obj.subject_visit.appointment.id))

    def view_on_site(self, obj):
            dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
                'subject_dashboard_url')
            try:
                url = reverse(
                    dashboard_url_name, kwargs=dict(
                        subject_identifier=obj.subject_visit.subject_identifier,
                        appointment=str(obj.subject_visit.appointment.id)))
            except NoReverseMatch:
                url = super().view_on_site(obj)
            return url