from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField, DateField, DateTimeField, Model


class User(AbstractUser):
    is_patient = BooleanField(default=False)
    is_authorized_party = BooleanField(default=False)
    is_clinic_staff = BooleanField(default=False)
