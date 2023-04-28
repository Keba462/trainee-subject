# Generated by Django 4.2 on 2023-04-26 05:47

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_base.model_fields.custom_fields
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.model_validators.phone
import edc_base.sites.managers
import edc_base.utils
import edc_protocol.validators
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
        ('edc_appointment', '0016_alter_historicalappointment_options_and_more'),
        ('trainee_subject', '0004_historicalsubjectconsent_subjectconsent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectLocator',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, unique=True, verbose_name='Subject Identifier')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('may_call', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given permission <b>to contacted by telephone or cell</b> by study staff for follow-up purposes during the study?')),
                ('may_visit_home', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given permission for study staff <b>to make home visits</b> for follow-up purposes?')),
                ('may_sms', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='Has the participant given permission <b>to be contacted by SMS</b> by study staff for follow-up purposes during the study?')),
                ('mail_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Mailing address ')),
                ('physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Physical address with detailed description')),
                ('subject_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('subject_cell_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('subject_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone')),
                ('subject_phone_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone (alternate)')),
                ('may_contact_indirectly', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='For example a partner, spouse, family member, neighbour ...', max_length=25, verbose_name='Has the participant given permission for study staff <b>to contact anyone else</b> for follow-up purposes during the study?')),
                ('indirect_contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full names of the contact person')),
                ('indirect_contact_relation', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('indirect_contact_physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Full physical address ')),
                ('indirect_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('indirect_contact_cell_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternative)')),
                ('indirect_contact_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('subject_work_place', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Name and location of work place')),
                ('subject_work_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Work contact telephone')),
                ('subject_work_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Work contact cell number')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('date_signed', models.DateField(default=django.utils.timezone.now, validators=[edc_base.model_validators.date.date_not_future], verbose_name='Date Locator Form signed ')),
                ('local_clinic', models.CharField(help_text='Please give clinic code.', max_length=75, verbose_name='Which health facility do you normally go to, in this village?')),
                ('home_village', models.CharField(max_length=75, verbose_name='Where is your home village?')),
                ('has_alt_contact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='If we are unable to contact the person indicated above, is there another individual (including next of kin) with whom the study team can get in contact with?')),
                ('alt_contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='include firstname and lastname (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full Name of the responsible person')),
                ('alt_contact_rel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('other_alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('alt_contact_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('may_call_work', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('doesnt_work', 'Does not work')], max_length=25, verbose_name='Has the participant given permission to contacted <b>at work</b> by telephone or cell by study staff for follow-up purposes during the study?')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subject_locator_site', to='sites.site')),
            ],
            options={
                'verbose_name': 'Subject Locator',
            },
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSubjectVisit',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('visit_schedule_name', models.CharField(editable=False, help_text='the name of the visit schedule used to find the "schedule"', max_length=25)),
                ('schedule_name', models.CharField(editable=False, max_length=25)),
                ('visit_code', models.CharField(editable=False, max_length=25, null=True)),
                ('visit_code_sequence', models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of this report', validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Visit Date and Time')),
                ('reason_unscheduled_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for unscheduled visit, specify')),
                ('reason_missed', models.CharField(blank=True, max_length=35, null=True, verbose_name="If 'Missed' above, provide the reason the scheduled visit was missed")),
                ('reason_missed_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for missed visit, specify')),
                ('study_status', models.CharField(max_length=50, null=True, verbose_name="What is the participant's current study status")),
                ('require_crfs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10, verbose_name='Are scheduled data being submitted with this visit?')),
                ('info_source_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If "Other" source of information, specify')),
                ('survival_status', models.CharField(choices=[('alive', 'Alive'), ('dead', 'Deceased'), ('unknown', 'Unknown')], default='alive', max_length=10, null=True, verbose_name="Participant's survival status")),
                ('last_alive_date', models.DateField(blank=True, null=True, validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Date participant last known alive')),
                ('comments', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment if any additional pertinent information about the participant')),
                ('reason', models.CharField(choices=[('initial_visit/contact', 'Initial visit/contact'), ('fu_visit/contact', 'Follow up visit/contact'), ('unscheduled_visit/contact', 'Unscheduled visit/contact'), ('missed_visit', 'Missed visit'), ('death', 'Death'), ('off study', 'Off study (use only when taking subject off study)'), ('deferred', 'Deferred')], max_length=25, verbose_name='What is the reason for this visit report?')),
                ('reason_unscheduled', models.CharField(choices=[('routine_oncology', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'), ('ill_oncology', 'Ill oncology clinic visit'), ('patient_called', 'Patient called to come for visit'), ('N/A', 'Not Applicable'), ('OTHER', 'Other, specify:')], default='N/A', max_length=50, verbose_name="If 'Unscheduled' above, provide reason for the unscheduled visit")),
                ('info_source', models.CharField(choices=[('clinic_visit', 'Clinic visit with participant'), ('other_contact_subject', 'Other contact with participant (i.e telephone call)'), ('contact_health worker', 'Contact with health care worker'), ('contact_family/designated_person', 'Contact with family or designated person who can provide information'), ('OTHER', 'Other,specify')], max_length=40, verbose_name='What is the main source of this information?')),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('appointment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_appointment.appointment')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Visit',
                'verbose_name_plural': 'historical Subject Visits',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubjectLocator',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(db_index=True, max_length=50, verbose_name='Subject Identifier')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('may_call', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given permission <b>to contacted by telephone or cell</b> by study staff for follow-up purposes during the study?')),
                ('may_visit_home', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given permission for study staff <b>to make home visits</b> for follow-up purposes?')),
                ('may_sms', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='Has the participant given permission <b>to be contacted by SMS</b> by study staff for follow-up purposes during the study?')),
                ('mail_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Mailing address ')),
                ('physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Physical address with detailed description')),
                ('subject_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('subject_cell_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('subject_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone')),
                ('subject_phone_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone (alternate)')),
                ('may_contact_indirectly', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='For example a partner, spouse, family member, neighbour ...', max_length=25, verbose_name='Has the participant given permission for study staff <b>to contact anyone else</b> for follow-up purposes during the study?')),
                ('indirect_contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full names of the contact person')),
                ('indirect_contact_relation', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('indirect_contact_physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Full physical address ')),
                ('indirect_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('indirect_contact_cell_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternative)')),
                ('indirect_contact_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('subject_work_place', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Name and location of work place')),
                ('subject_work_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Work contact telephone')),
                ('subject_work_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Work contact cell number')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('date_signed', models.DateField(default=django.utils.timezone.now, validators=[edc_base.model_validators.date.date_not_future], verbose_name='Date Locator Form signed ')),
                ('local_clinic', models.CharField(help_text='Please give clinic code.', max_length=75, verbose_name='Which health facility do you normally go to, in this village?')),
                ('home_village', models.CharField(max_length=75, verbose_name='Where is your home village?')),
                ('has_alt_contact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='If we are unable to contact the person indicated above, is there another individual (including next of kin) with whom the study team can get in contact with?')),
                ('alt_contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='include firstname and lastname (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full Name of the responsible person')),
                ('alt_contact_rel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('other_alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('alt_contact_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('may_call_work', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('doesnt_work', 'Does not work')], max_length=25, verbose_name='Has the participant given permission to contacted <b>at work</b> by telephone or cell by study staff for follow-up purposes during the study?')),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Locator',
                'verbose_name_plural': 'historical Subject Locators',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='SubjectVisit',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('visit_schedule_name', models.CharField(editable=False, help_text='the name of the visit schedule used to find the "schedule"', max_length=25)),
                ('schedule_name', models.CharField(editable=False, max_length=25)),
                ('visit_code', models.CharField(editable=False, max_length=25, null=True)),
                ('visit_code_sequence', models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of this report', validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Visit Date and Time')),
                ('reason_unscheduled_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for unscheduled visit, specify')),
                ('reason_missed', models.CharField(blank=True, max_length=35, null=True, verbose_name="If 'Missed' above, provide the reason the scheduled visit was missed")),
                ('reason_missed_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for missed visit, specify')),
                ('study_status', models.CharField(max_length=50, null=True, verbose_name="What is the participant's current study status")),
                ('require_crfs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10, verbose_name='Are scheduled data being submitted with this visit?')),
                ('info_source_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If "Other" source of information, specify')),
                ('survival_status', models.CharField(choices=[('alive', 'Alive'), ('dead', 'Deceased'), ('unknown', 'Unknown')], default='alive', max_length=10, null=True, verbose_name="Participant's survival status")),
                ('last_alive_date', models.DateField(blank=True, null=True, validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Date participant last known alive')),
                ('comments', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment if any additional pertinent information about the participant')),
                ('reason', models.CharField(choices=[('initial_visit/contact', 'Initial visit/contact'), ('fu_visit/contact', 'Follow up visit/contact'), ('unscheduled_visit/contact', 'Unscheduled visit/contact'), ('missed_visit', 'Missed visit'), ('death', 'Death'), ('off study', 'Off study (use only when taking subject off study)'), ('deferred', 'Deferred')], max_length=25, verbose_name='What is the reason for this visit report?')),
                ('reason_unscheduled', models.CharField(choices=[('routine_oncology', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'), ('ill_oncology', 'Ill oncology clinic visit'), ('patient_called', 'Patient called to come for visit'), ('N/A', 'Not Applicable'), ('OTHER', 'Other, specify:')], default='N/A', max_length=50, verbose_name="If 'Unscheduled' above, provide reason for the unscheduled visit")),
                ('info_source', models.CharField(choices=[('clinic_visit', 'Clinic visit with participant'), ('other_contact_subject', 'Other contact with participant (i.e telephone call)'), ('contact_health worker', 'Contact with health care worker'), ('contact_family/designated_person', 'Contact with family or designated person who can provide information'), ('OTHER', 'Other,specify')], max_length=40, verbose_name='What is the main source of this information?')),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='edc_appointment.appointment')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Subject Visit',
                'ordering': ('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'visit_code_sequence', 'report_datetime'),
                'abstract': False,
                'unique_together': {('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'visit_code_sequence'), ('subject_identifier', 'visit_schedule_name', 'schedule_name', 'report_datetime')},
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
