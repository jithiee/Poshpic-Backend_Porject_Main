# Generated by Django 5.0.2 on 2024-02-23 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("follow", "0016_alter_follow_create_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="create_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 23, 14, 50, 22, 981320)
            ),
        ),
    ]
