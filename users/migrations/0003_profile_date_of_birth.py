# Generated by Django 3.2.3 on 2021-06-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20210602_2009"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]