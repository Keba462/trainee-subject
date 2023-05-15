from django.contrib import admin
from trainee_subject.admin.model_admin_mixins import CrfModelAdminMixin
from trainee_subject.forms.education_questionaire_form import EducationQuestionaireForm
from trainee_subject.models.educational_questionaire import EducationalQuestionaire
from ..admin_site import trainee_subject_admin


@admin.register(EducationalQuestionaire, site=trainee_subject_admin)
class EducationQuestionaireAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationQuestionaireForm
    fields = (
        "subject_visit",
        "working",
        "work_type",
        "occupation",
        "salary")
    radio_fields = {
        "working": admin.VERTICAL,
        "work_type": admin.VERTICAL,
        "occupation": admin.VERTICAL,
        "salary": admin.VERTICAL}