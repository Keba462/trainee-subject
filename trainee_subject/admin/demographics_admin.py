from django.contrib import admin
from trainee_subject.admin.model_admin_mixins import CrfModelAdminMixin
from trainee_subject.forms.demographics_form import DemographicForm
from trainee_subject.models.demographics import Demographic
from ..admin_site import trainee_subject_admin


@admin.register(Demographic, site=trainee_subject_admin)
class DemographicAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = DemographicForm
    fields = (
        "subject_visit",
        "marital_status",
        "women_number_husbands",
        "men_number_wives",
        "housemate")
    radio_fields = {
        "marital_status": admin.VERTICAL,
        "housemate": admin.VERTICAL}