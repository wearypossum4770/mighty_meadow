import pytest
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from users.models import Address, Profile


@pytest.mark.asyncio
class TestSiteOperation(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_homepage_connection(self):
        homepage = self.client.get("/")
        assert homepage.status_code == 200


data = {
    "first_name": "ichigo",
    "last_name": "kurosaki",
    "password": "RzMdsJLufx2FvVi",
    "email": "ichigo.kurosaki@soul.society.com",
    "username": "ichigo.kurosaki",
}


@pytest.mark.django_db
def profile_obj():
    profile = Profile.objects.create(
        user=get_user_model().objects.create_user(
            first_name="john",
            middle_name="John",
            last_name="Trump",
            suffix="Sr",
            password="RzMdsJLufx2FvVi",
            username="john.john.trump.sr",
            email="john.john.trump.sr@us.presidents.com",
        )
    )
    profile.addresses.create(
        idempotent_key="ckpfzqd7l0000nbve3vq1hfgl",
        address_type="RESD",
        street1="1600 Pennsylvania Avenue NW",
        street2="",
        state="Washington",
        city="DC",
        zipcode="20500",
    )


pytestmark = pytest.mark.django_db


class TestProfile(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        profile_obj()
        cls.profile = Profile.objects.get(
            user=get_user_model().objects.get(username="john.john.trump.sr")
        )
        cls.address = cls.profile.addresses.all()[0]

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_user_profile_first_name(self):
        assert self.profile.user.first_name == "john"

    def test_user_profile_middle_name(self):
        assert self.profile.user.middle_name == "John"

    def test_user_profile_last_name(self):
        assert self.profile.user.last_name == "Trump"

    def test_user_profile_suffix(self):
        assert self.profile.user.suffix == "Sr"

    def test_user_profile_password(self):
        assert self.profile.user.password == self.profile.user.password

    def test_user_profile_username(self):
        assert self.profile.user.username == "john.john.trump.sr"

    def test_user_profile_email(self):
        assert self.profile.user.email == "john.john.trump.sr@us.presidents.com"

    def test_profile_image(self):
        assert self.profile.image.name == "default.webp"

    def test_profile_internal_notes(self):
        assert self.profile.internal_notes == ""

    def test_address_idempotent_key(self):
        assert self.address.idempotent_key == "ckpfzqd7l0000nbve3vq1hfgl"

    def test_address_address_type(self):
        assert self.address.address_type == "RESD"

    def test_address_street1(self):
        assert self.address.street1 == "1600 Pennsylvania Avenue NW"

    def test_address_street2(self):
        assert self.address.street2 == ""

    def test_address_state(self):
        assert self.address.state == "Washington"

    def test_address_city(self):
        assert self.address.city == "DC"

    def test_address_zipcode(self):
        assert self.address.zipcode == "20500"


pytestmark = pytest.mark.django_db


class TestStaffUser(TestCase):
    fixtures = ("userinit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        profile_obj()
        cls.staff_user = get_user_model().objects.get(pk=46)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_is_staff(self):
        assert self.staff_user.is_staff == True

    def test_is_active(self):
        assert self.staff_user.is_active == True

    def test_is_patient(self):
        assert self.staff_user.is_patient == False

    def test_is_authorized_party(self):
        assert self.staff_user.is_authorized_party == False

    def test_is_clinic_staff(self):
        assert self.staff_user.is_clinic_staff == False

    def test_first_name(self):
        assert self.staff_user.first_name == "Joseph"

    def test_middle_name(self):
        assert self.staff_user.middle_name == "Robinette"

    def test_last_name(self):
        assert self.staff_user.last_name == "Biden"

    def test_suffix(self):
        assert self.staff_user.suffix == "Jr"

    def test_username(self):
        assert self.staff_user.username == "joseph.robinette.biden.jr"

    def test_email(self):
        assert self.staff_user.email == "joseph.robinette.biden.jr@us.presidents.com"
