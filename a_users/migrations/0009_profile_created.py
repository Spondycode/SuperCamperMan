# Generated by Django 5.0.3 on 2024-04-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("a_users", "0008_remove_profile_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]