# Generated by Django 4.1.4 on 2022-12-24 09:39

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="default-profile.png",
                null=True,
                upload_to=accounts.models.custom_file_name,
            ),
        ),
    ]
