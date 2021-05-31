from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, *args, **kwargs):
    print(sender)
    print(instance)
    print(args)
    print(kwargs)
    if created:
        Profile.objects.create(user=instance)

    instance.profile.save()
