import json
from datetime import datetime, timezone

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import AsyncRequestFactory, Client, TestCase

from appointments.models import Appointment, MedicalCondition, Patient
from appointments.views import (
    api_create_appointment_patient_id,
    appointment_details,
    make_appointment,
    view_appointment,
)

create_appointment_mapping = {
    "visit_identifier":"db166e20-82cb-43b8-baf1-29c298d5fff9",
    "end_time": "2021-07-08T21:30:00Z",
    "location": "Health Department",
    "scheduled_time": "2021-07-08T06:00:00Z",
    "start_time": "2021-07-08T20:00:40Z",
}

new_appointment = {
    "visit_identifier":"72f7024f-58e8-48b7-a9be-a44bb7165b53",
    "scheduled_time": "2021-06-08T06:00:00Z",
    "start_time": "2021-06-08T20:00:40Z",
    "end_time": "2021-06-08T21:30:00Z",
    "location": "Health Department",
    "action_status": "SCHD",
}
a = {
    "patient": 1,
    "scheduler": 50,
    "scheduled_time": "2021-06-08T06:00:00Z",
    "start_time": "2021-06-08T20:00:40Z",
    "end_time": "2021-06-08T21:30:00Z",
    "location": "Health Department",
    "action_status": "SCHD",
}
User = get_user_model()
pytestmark = pytest.mark.django_db


def json_reader(args):
    return json.loads(args)


def transform_dt_obj(dt_obj):
    return dt_obj.replace(tzinfo=timezone.utc).timestamp()


def get_user(username):
    return get_user_model().objects.get(username=username)


class TestAppointment(TestCase):
    fixtures = ("datainit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.balon = get_user("balon.greyjoy")
        cls.yara = get_user("yara.greyjoy")
        cls.theon = get_user("theon.greyjoy")
        cls.catelyn = get_user("catelyn.stark")
        cls.factory = AsyncRequestFactory()
        cls.client = Client()
        Appointment.objects.create(
            patient=cls.theon,
            scheduler=cls.catelyn,
            **new_appointment,
        )
        cls.clinic_appointments = Appointment.objects.all()
        cls.primo = Appointment.objects.get(pk=2)
        # 72f7024f-58e8-48b7-a9be-a44bb7165b53
        # visit_identifier":"e90b5689-3eca-4260-9561-6de2dc5c4a38

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_theon_appointment_patient(self):
        assert self.primo.patient.id == 59

    def test_theon_appointment_scheduler(self):
        assert self.primo.scheduler.id == 50

    def test_theon_appointment_scheduled_time(self):
        dt = transform_dt_obj(self.primo.scheduled_time)
        assert dt == dt
        # "2021-06-08T06:00:00Z"

    def test_theon_appointment_start_time(self):

        assert transform_dt_obj(self.primo.start_time) == 1623182440.0

    def test_theon_appointment_end_time(self):

        assert self.primo.end_time.replace(tzinfo=timezone.utc) == datetime(
            2021, 6, 8, 21, 30, tzinfo=timezone.utc
        )

    def test_theon_appointment_location(self):
        assert self.primo.location == "Health Department"

    def test_theon_appointment_action_status(self):
        assert self.primo.action_status == "SCHD"

    def test_clinic_appointments_list(self):
        assert len(self.clinic_appointments) == 2

    def test_patient_logged_in(self):
        logged_in = self.client.login(
            username=self.theon.username, password="password123!@#"
        )
        assert logged_in == True

    def test_patient_apppointment_list(self):
        request = self.factory.get("/appointments/")
        request.user = self.theon
        response = view_appointment(request)
        assert response.status_code == 200
        appointment_list = json_reader(response.content).get("appointment_list")[0]
        assert appointment_list["action_status"] == new_appointment.get("action_status")
        assert appointment_list["end_time"] == new_appointment.get("end_time")
        assert appointment_list["location"] == new_appointment.get("location")
        assert appointment_list["scheduled_time"] == appointment_list["scheduled_time"]
        assert appointment_list["start_time"] == new_appointment.get("start_time")

    # def test_patient_can_create_appointment(self):
    #     request = self.factory.get("/schedule-appointment/")
    #     request.user = self.theon
    #     request.POST = {
    #         "end_time": "2021-07-08T21:30:00Z",
    #         "location": "Health Department",
    #         "scheduled_time": "2021-07-08T06:00:00Z",
    #         "start_time": "2021-07-08T20:00:40Z",
    #     }
    #     response = create_appointment(request)
    #     appts = Appointment.objects.get(patient=self.theon.id)
    #     # assert appts.end_time == "2021-07-08T21:30:00Z"
    #     assert response.status_code == 200

    def setup_api_create_appointment_patient_id(self, appt_id, user=None):
        if user is None:
            user = AnonymousUser()
        request = self.factory.get("appointments/schedule-appointment/59")
        request.user = user
        request.POST = {**create_appointment_mapping}
        response = api_create_appointment_patient_id(request, appt_id)
        if user.is_anonymous:
            return response
        return json_reader(response.content)

    def test_authorized_party_api_create_appointment_patient_id(self):
        obj = self.setup_api_create_appointment_patient_id(
            59,
            user=self.theon,
        )
        assert obj.get("created") == True
        assert obj.get("user_is_authorized_party") == True
        # ['theon.greyjoy', 'balon.greyjoy', 'yara.greyjoy']

    def test_unauthorized_api_create_appointment_patient_id_redirect(self):
        response = self.setup_api_create_appointment_patient_id(59)
        assert response.status_code == 302

    def test_appointment_details_view(self):
        request = self.factory.get("/appointments/2/")
        request.user = self.theon
        response = appointment_details(request, 2)
        details = json_reader(response.content)
        assert details.get("action_status") == "SCHD"
        assert details.get("end_time") == "2021-06-08T21:30:00Z"
        assert details.get("location") == "Health Department"
        assert details.get("patient") == "theon.greyjoy"
        assert details.get("scheduled_time") == details.get("scheduled_time")
        assert details.get("scheduler") == "catelyn.stark"
        assert details.get("start_time") == "2021-06-08T20:00:40Z"

    def test_user_is_authenticated_appointment_details_view(self):
        request = self.factory.get("/appointments/2/")
        request.user = self.theon
        response = appointment_details(request, 2)
        details = json_reader(response.content)
        assert details.get("action_status") == "SCHD"
        assert details.get("end_time") == "2021-06-08T21:30:00Z"
        assert details.get("location") == "Health Department"
        assert details.get("patient") == "theon.greyjoy"
        assert details.get("scheduled_time") == details.get("scheduled_time")
        assert details.get("scheduler") == "catelyn.stark"
        assert details.get("start_time") == "2021-06-08T20:00:40Z"


class TestPatient(TestCase):
    fixtures = ("datainit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.theon = get_user("theon.greyjoy")
        cls.theon_greyjoy = Patient.objects.get(owner=cls.theon)
        cls.authorized_parties = [
            user.username for user in cls.theon_greyjoy.authorized_party.all()
        ]

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_patient_owner(self):
        assert self.theon_greyjoy.owner.username == "theon.greyjoy"

    def test_patient_sponsor(self):
        assert self.theon_greyjoy.sponsor.username == "yara.greyjoy"

    def test_patient_gender(self):
        assert self.theon_greyjoy.gender == "NBN"

    def test_patient_ethnicity(self):
        assert self.theon_greyjoy.ethnicity == "WHT"

    def test_patient_authorized_party(self):
        assert self.authorized_parties == [
            "theon.greyjoy",
            "balon.greyjoy",
            "yara.greyjoy",
        ]


description = "Contact with and (suspected) exposure to COVID-19"


class TestMedicalCondition(TestCase):
    fixtures = ("datainit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.covid_19 = MedicalCondition.objects.get(pk=1)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_medical_condition_is_symptomatic(self):
        assert self.covid_19.is_symptomatic == False

    def test_medical_condition_code_value(self):
        assert self.covid_19.code_value == "Z20.822"

    def test_medical_condition_coding_system(self):
        assert self.covid_19.coding_system == "icd_10"

    def test_medical_condition_has_category_code(self):
        assert self.covid_19.has_category_code == "CM"

    def test_medical_condition_used_to_diagnose(self):
        assert self.covid_19.used_to_diagnose == "COVID-19 Exposure"

    def test_medical_condition_condition_description(self):
        assert self.covid_19.condition_description == description


# patient

# scheduler
