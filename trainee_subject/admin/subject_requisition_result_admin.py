from django.contrib import admin
from edc_senaite_interface.admin import SenaiteResultAdminMixin
from ..admin_site import trainee_subject_admin
from ..forms import SubjectRequisitionResultForm
from ..models import SubjectRequisitionResult



@admin.register(SubjectRequisitionResult,site=trainee_subject_admin)
class SubjectRequisitionResultAdmin(SenaiteResultAdminMixin,admin.ModelAdmin):
    
    form = SubjectRequisitionResultForm