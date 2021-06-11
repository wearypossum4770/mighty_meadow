# Generated by Django 3.2.4 on 2021-06-08 16:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("appointments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="authorized_party",
            field=models.ManyToManyField(
                related_name="authorized_party", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="patient",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patient",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="patient",
            name="sponsor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="guarantor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="appointments.patient"
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="scheduler",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]