# Generated by Django 5.0.3 on 2024-03-31 19:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_inbox", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=100,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
