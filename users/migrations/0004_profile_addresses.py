# Generated by Django 3.2.3 on 2021-05-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="addresses",
            field=models.ManyToManyField(to="users.Address"),
        ),
    ]