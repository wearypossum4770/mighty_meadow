from cuid import cuid
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    ImageField,
    ManyToManyField,
    Model,
    OneToOneField,
    TextChoices,
    Q,
    TextField,
    CheckConstraint,
)
from datetime import datetime, timedelta
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
    middle_name = CharField(max_length=20, blank=True, null=True)
    title = CharField(max_length=20, blank=True, null=True)
    suffix = CharField(max_length=10, blank=True, null=True)
    date_of_birth = DateField(blank=True, null=True)
    is_patient = BooleanField(default=False)
    is_authorized_party = BooleanField(default=False)
    is_clinic_staff = BooleanField(default=False)
    date_of_death = DateField(null=True, blank=True)
    class Meta:
        constraints = [
            CheckConstraint(check=Q(date_of_death__lte=datetime.today()+timedelta(days=1)), name='not_dead_tomorrow'),
            CheckConstraint(check=Q(date_of_birth__lte=datetime.today()), name='born_before_today'),
        
        ]        
    def __str__(self):
        return f"Profile For {self.fist_name}"
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


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(upload_to="raw_profile_pictures", default="default.webp")
    addresses = ManyToManyField(Address)
    internal_notes = TextField(default="")
