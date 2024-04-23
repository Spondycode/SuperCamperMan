# Generated by Django 5.0.3 on 2024-04-23 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("a_plot", "0002_campsite_alter_plot_campsite"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plot",
            name="campsite",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="campsites",
                to="a_plot.campsite",
            ),
        ),
    ]
