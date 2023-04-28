from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_constants.constants import ALIVE, YES, NO, ON_STUDY
from edc_constants.constants import PARTICIPANT, NEG, NOT_APPLICABLE
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
import faker
from model_mommy.recipe import Recipe, seq
from trainee_subject.models.subject_consent import SubjectConsent

from trainee_subject.models.subject_screening import SubjectScreening
from trainee_subject.models.verbal_consent import VerbalConsent

fake = Faker()

subjectscreening = Recipe(
    SubjectScreening,
    enrollment_interest=YES,
    citizen=YES,
    age_in_years=35,
    enrollment_site='molapowabojang_clinic',
)

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    consent_datetime=get_utcnow(),
    dob=(get_utcnow() - relativedelta(years=25)).date(),
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials='XX',
    gender='F',
    language='en',
    identity_type='OMANG',
    is_dob_estimated=NO,
    citizen=YES,
    version='1',
    consent_reviewed=YES,
    assessment_score=YES,
    verbal_script=YES,
    study_questions=YES,
)

verbalconsent = Recipe(
    VerbalConsent,)