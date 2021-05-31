import pytest
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from users.models import Profile

pytestmark = pytest.mark.django_db


class TestProfile(TestCase):
    fixtures = ("usersinit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.patient = get_user_model().objects.get(last_name="doe")
        cls.profiles = Profile.objects.all()
        cls.john = cls.profiles[0]
        cls.johns_addresses = cls.john.addresses.all()[0]
        cls.admin = Profile.objects.first()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_profile_list(self):
        assert len(self.profiles) > 0

    def test_user_john_doe_first_name(self):
        assert self.patient.first_name == "john"

    def test_user_john_doe_last_name(self):
        assert self.patient.last_name == "doe"

    def test_user_john_doe_email(self):
        assert self.patient.email == "john.d.doe@example.com"

    def test_user_john_doe_username(self):
        assert self.patient.username == "john.d.doe"

    def test_user_profile_john_doe_has_address_type(self):
        assert self.johns_addresses.address_type == "RESD"

    def test_user_profile_john_doe_has_street1(self):
        assert self.johns_addresses.street1 == "3183  Byrd Lane"

    def test_user_profile_john_doe_has_street2(self):
        assert self.johns_addresses.street2 == ""

    def test_user_profile_john_doe_has_state(self):
        assert self.johns_addresses.state == "NM"

    def test_user_profile_john_doe_has_city(self):
        assert self.johns_addresses.city == "Albuquerque"

    def test_user_profile_john_doe_has_zipcode(self):
        assert self.johns_addresses.zipcode == "87112"
