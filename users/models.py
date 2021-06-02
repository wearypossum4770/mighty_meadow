from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    ImageField,
    ManyToManyField,
    Model,TextField,
    OneToOneField,
    TextChoices,
)
from django.utils.translation import gettext_lazy as _
from cuid import cuid
User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    # middle_name=CharField(max_length=20, blank=True, null=True)
    # title=CharField(max_length=20, blank=True, null=True)
    # suffix
    is_patient = BooleanField(default=False)
    is_authorized_party = BooleanField(default=False)
    is_clinic_staff = BooleanField(default=False)

class Address(Model):
    class Type(TextChoices):
        MAIL = "MAIL", _("Mailing")
        RESIDENTIAL = "RESD", _("Residential")
        BUSINESS = "BUSN", _("Business")
    idempotent_key = CharField(max_length=50, default=cuid)
    address_type = CharField(max_length=4, choices=Type.choices)
    street1 = CharField(max_length=100)
    street2 = CharField(max_length=100, null=True, blank=True)
    state = CharField(max_length=4)
    city = CharField(max_length=50)
    zipcode = CharField(max_length=10)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(upload_to="raw_profile_pictures", default="default.webp")
    addresses = ManyToManyField(Address)
    internal_notes = TextField(default="")