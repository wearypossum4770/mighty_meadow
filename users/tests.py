from datetime import date, datetime, timedelta

import pytest
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from users.forms import UserRegisterForm
from users.models import Address, Profile


@pytest.mark.asyncio
@pytest.mark.django_db
class TestProfile(TestCase):
    fixtures = ("userinit.json",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.staff_user = get_user_model().objects.get(pk=46)
        Profile.objects.create(user=cls.staff_user)
        cls.profile = Profile.objects.get(user=cls.staff_user)
        cls.profile.addresses.create(
            idempotent_key="ckpfzqd7l0000nbve3vq1hfgl",
            address_type="RESD",
            street1="1600 Pennsylvania Avenue NW",
            street2="",
            state="Washington",
            city="DC",
            zipcode="20500",
        )
        cls.address = cls.profile.addresses.all()[0]

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_user_profile_first_name(self):
        assert self.staff_user.first_name == "Joseph"

    def test_user_profile_middle_name(self):
        assert self.staff_user.middle_name == "Robinette"

    def test_user_profile_last_name(self):
        assert self.staff_user.last_name == "Biden"

    def test_user_profile_suffix(self):
        assert self.staff_user.suffix == "Jr"

    def test_user_profile_password(self):
        assert self.staff_user.password == self.staff_user.password

    def test_user_profile_username(self):
        assert self.staff_user.username == "joseph.robinette.biden.jr"

    def test_user_profile_email(self):
        assert self.staff_user.email == "joseph.robinette.biden.jr@us.presidents.com"

    def test_profile_image(self):
        assert self.profile.image.name == "default.webp"

    def test_profile_internal_notes(self):
        assert self.profile.internal_notes == ""

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


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = "RzMdsJLufx2FvVi"
        return django_user_model.objects.create_user(**kwargs)

    return make_user


data = {
    "first_name": "ichigo",
    "last_name": "kurosaki",
    "random": "something",
    "password1": "RzMdsJLufx2FvVi",
    "password2": "RzMdsJLufx2FvVi",
    "email": "ichigo.kurosaki@soul.society.com",
    "username": "ichigo.kurosaki",
}


@pytest.mark.asyncio
@pytest.mark.django_db
def test_auth_view(client, create_user, test_password):
    user = create_user()
    url = reverse("login")
    client.login(username=user.username, password=test_password)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.django_db
class TestSiteOperation(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = UserRegisterForm(data)
        cls.is_valid = cls.form.is_valid()
        cls.form.save()
        cls.client = Client()
        cls.about = cls.client.get("/about/")
        cls.homepage = cls.client.get("/")
        cls.admin = cls.client.login(username="admin", password="secret")
        cls.patient = cls.client.login(username="patient_client", password="secret")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_homepage_page_connection(self):
        assert self.homepage.status_code == 200

    def test_about_page_connection(self):
        assert self.about.status_code == 200

    def test_user_registered(self):
        new_registrant = get_user_model().objects.get(username="ichigo.kurosaki")
        assert new_registrant is not None

    def test_user_instance_was_saved(self):
        assert self.form.instance.username == "ichigo.kurosaki"

    def test_user_form_is_valid(self):
        assert self.is_valid == True
