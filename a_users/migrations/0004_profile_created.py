# Generated by Django 5.0.3 on 2024-04-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_users", "0003_alter_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
