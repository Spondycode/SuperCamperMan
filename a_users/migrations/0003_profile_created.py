# Generated by Django 5.0.3 on 2024-03-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "a_users",
            "0002_profile_campermode_profile_camperstory_profile_email_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
