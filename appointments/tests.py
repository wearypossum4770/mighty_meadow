import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

from appointments.models import Appointment, MedicalCondition, Patient

User = get_user_model()
pytestmark = pytest.mark.django_db

class TestAppointment(TestCase):
    fixtures = ("datainit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.balon = get_user_model().objects.get(username =  "balon.greyjoy")
        cls.yara = get_user_model().objects.get(username = "yara.greyjoy")
        cls.theon = get_user_model().objects.get(username = "theon.greyjoy")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
    
    def test_patient_can_create_appointment(self):
        ...
    def test_staff_member_can_create_appointment(self):
        ...
    
class TestPatient(TestCase):
    fixtures = ("datainit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.theon = get_user_model().objects.get(username="theon.greyjoy")
        cls.theon_greyjoy = Patient.objects.get(owner=cls.theon)
        cls.authorized_parties = [user.username for user in cls.theon_greyjoy.authorized_party.all()]
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
        assert self.authorized_parties  == ['theon.greyjoy', 'balon.greyjoy', 'yara.greyjoy']

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
