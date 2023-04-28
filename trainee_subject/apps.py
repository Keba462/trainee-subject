from django.apps import AppConfig as DjangoConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_device.device_permission import DeviceAddPermission, DeviceChangePermission,DevicePermissions
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from edc_device.constants import CENTRAL_SERVER, CLIENT, NODE_SERVER
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_visit_tracking.apps import (AppConfig as BaseEdcVisitTrackingAppConfig)

class AppConfig(DjangoConfig):
    name = 'trainee_subject'
    verbose_name = "Trainee Subject +Crfs"
    admin_site_name = 'trainee_subject_admin'


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}

class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
        use_settings = True
        device_permissions = DevicePermissions(
            DeviceAddPermission(
                model='plot.plot',
                device_roles=[CENTRAL_SERVER, CLIENT]),
            DeviceChangePermission(
                model='plot.plot',
                device_roles=[NODE_SERVER, CENTRAL_SERVER, CLIENT]))
        

class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        apply_community_filter = True
        send_sms_reminders = True
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='trainee_subject.subjectvisit')
        ]

class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'trainee_subject': (
                'subject_visit', 'trainee_subject.subjectvisit')}