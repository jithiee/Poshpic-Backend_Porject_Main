# Generated by Django 5.0.2 on 2024-02-17 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("follow", "0014_alter_follow_create_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="create_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 17, 13, 59, 58, 853577)
            ),
        ),
    ]