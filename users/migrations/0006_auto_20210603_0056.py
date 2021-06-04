# Generated by Django 3.2.3 on 2021-06-03 00:56

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_date_of_death"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "date_of_death__lt",
                        datetime.datetime(2021, 6, 3, 0, 56, 54, 632770),
                    )
                ),
                name="age_gte_18",
            ),
        ),
    ]