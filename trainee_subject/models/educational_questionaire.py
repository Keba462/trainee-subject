from django.db import models
from edc_constants.choices import YES_NO

from trainee_subject.models.subject_visit import SubjectVisit
from ..choices import OCCUPATION, SALARY, WORK_TYPE
from edc_reference.model_mixins import ReferenceModelMixin
from trainee_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class EducationalQuestionaire(CrfModelMixin,ReferenceModelMixin):

    subject_visit = models.ForeignKey(SubjectVisit)
   
    working = models.CharField(
        verbose_name= "Are you currently working ?",
        max_length=11,
        choices=YES_NO,
    )


    work_type = models.CharField(
        verbose_name= "In your main job what type of work do you do ?",
        max_length=100,
        choices=WORK_TYPE,

    )

    occupation = models.CharField(
        verbose_name= "Describe the work that you do or did in your most recent job",
        max_length=100,
        choices=OCCUPATION,
    )

    salary = models.CharField(
        verbose_name="In the past month, how much money did you earn from work you did or received in payment?",
        max_length=150,
        choices=SALARY,

    )


    class Meta:
        app_label = 'trainee_subject'
        verbose_name = 'Educational Questionaire'
