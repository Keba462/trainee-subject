from django.contrib import admin
from trainee_subject.admin.model_admin_mixin import CrfModelAdminMixin
from trainee_subject.forms.community_engagement_form import CommunityEngagementForm
from trainee_subject.models.community_engagement import CommunityEngagement
from ..admin_site import trainee_subject_admin


@admin.register(CommunityEngagement, site=trainee_subject_admin)
class CommunityEngagementAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = CommunityEngagementForm
    fields = (
        "subject_visit",
        "community_activity",
        "voting_status",
        "major_problems",
        "problem_solving")
    radio_fields = {
        "community_activity": admin.VERTICAL,
        "voting_status": admin.VERTICAL,
        "major_problems": admin.VERTICAL,
        "problem_solving": admin.VERTICAL}