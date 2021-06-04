from datetime import datetime, timedelta

from cuid import cuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    CheckConstraint,
    DateField,
    DateTimeField,
    ImageField,
    ManyToManyField,
    Model,
    OneToOneField,
    Q,
    TextChoices,
    TextField,
)
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL
# Testing ideas https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


def validate_date_of_birth(is_patient, value=None):
    if is_patient and value is None:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )


class User(AbstractUser):
    first_name =CharField(max_length=100, blank=True, null=True)
    last_name =CharField(max_length=100, blank=True, null=True)
    middle_name = CharField(max_length=20, blank=True, null=True)
    title = CharField(max_length=20, blank=True, null=True)
    suffix = CharField(max_length=10, blank=True, null=True)
    date_of_birth = DateField(blank=True, null=True)
    is_patient = BooleanField(default=False)
    is_authorized_party = BooleanField(default=False)
    is_clinic_staff = BooleanField(default=False)
    date_of_death = DateField(null=True, blank=True)
    retention_only =BooleanField(default=False)
    # internal_notes = TextField(default="", null=True, blank=True)
    @property
    def mark_retention_only(self):
        if datetime.today()>self.date_of_death:
            self.retention_only = True
        return ""
    @property
    def full_name(self):
        full_name = ""
        if self.first_name:
            full_name += f" {self.first_name}"
        if self.middle_name:
            full_name += f" {self.middle_name}"
        if self.last_name:
            full_name += f" {self.last_name}"
        return full_name

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(date_of_death__lte=datetime.today() + timedelta(days=1)),
                name="not_dead_tomorrow",
            ),
            CheckConstraint(
                check=Q(date_of_birth__lte=datetime.today()), name="born_before_today"
            ),
        ]

    def __str__(self):
        return f"User account: {self.first_name} {self.middle_name} {self.last_name}"

    @property
    def require_date_of_birth(self):
        validate_date_of_birth(self.user.is_patient, self.date_of_birth)
        return "Patient has date of birth"


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

    def __str__(self):
        return f" {self.street1}  {self.city},  {self.state}  {self.zipcode}"


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(upload_to="raw_profile_pictures", default="default.webp")
    addresses = ManyToManyField(Address, blank=True)
    internal_notes = TextField(default="", null=True, blank=True)

    def __str__(self):
        return f" {self.user.full_name}"
