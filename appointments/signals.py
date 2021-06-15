from uuid import uuid4

from cuid import cuid
from django.db.models.signals import post_save
from django.dispatch import receiver

from appointments.models import Appointment


@receiver(post_save, sender=Appointment)
def create_external_identifier(sender, instance, created, *args, **kwargs):
    if created and instance.external_identifier is None:
        instance.external_identifier = f"{uuid4()}_{cuid()}"
        instance.save()
