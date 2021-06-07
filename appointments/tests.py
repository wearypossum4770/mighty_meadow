import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

from appointments.models import Appointment, Patient

User = get_user_model()
pytestmark = pytest.mark.django_db

# class TestAppointment(TestCase):
#     fixtures = ("userinit.json",)

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#     @classmethod
#     def tearDownClass(cls):
#         super().tearDownClass()
class TestPatient(TestCase):
    fixtures = ("userinit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.theon_greyjoy = Patient.objects.get(
            owner=get_user_model().objects.get(username="theon.greyjoy")
        )

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


# patient

# scheduler
