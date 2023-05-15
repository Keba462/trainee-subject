from django.db import models
from trainee_subject.choices import COMMUNITY_ACTIVITY, MAJOR_COMMUNITY_PROBLEMS, YES_NO_NA_DA,YES_NO_DK_DA
from trainee_subject.models.model_mixins.crf_model_mixin import CrfModelMixin
from edc_reference.model_mixins import ReferenceModelMixin

from trainee_subject.models.subject_visit import SubjectVisit

class CommunityEngagement(CrfModelMixin,ReferenceModelMixin):

    subject_visit = models.ForeignKey(SubjectVisit)

    community_activity = models.CharField(
        verbose_name= ("How active are you in community activities such as burial society,"),
        max_length=50,
        choices=COMMUNITY_ACTIVITY,
        help_text= ("Examples are Motshelo, Syndicate,PTA, VDC(Village Development Committee)," 
                       "Mophato and development of the community that surrounds you?")
    )

    voting_status = models.CharField(
        verbose_name= "Did you vote in the last local government election ?",
        choices=YES_NO_NA_DA,
        max_length=21,

    )
    
    major_problems = models.CharField(
        verbose_name="What are the major problems in this neighborhood?",
        choices= MAJOR_COMMUNITY_PROBLEMS,
        max_length=50,


    )

    problem_solving =models.CharField(
        verbose_name="If there is a problem in this neighborhood,do the adults work together in solving it?",
        choices=YES_NO_DK_DA,
        max_length=50,
        
    )

    class Meta:
        app_label = 'trainee_subject'
        verbose_name = 'Community Engagement'
        