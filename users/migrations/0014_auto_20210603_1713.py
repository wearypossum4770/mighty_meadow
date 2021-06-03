# Generated by Django 3.2.4 on 2021-06-03 17:13

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_auto_20210603_1537"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="user",
            name="not_dead_tomorrow",
        ),
        migrations.RemoveConstraint(
            model_name="user",
            name="born_before_today",
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "date_of_death__lte",
                        datetime.datetime(2021, 6, 4, 17, 13, 1, 23585),
                    )
                ),
                name="not_dead_tomorrow",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "date_of_birth__lte",
                        datetime.datetime(2021, 6, 3, 17, 13, 1, 23601),
                    )
                ),
                name="born_before_today",
            ),
        ),
    ]
