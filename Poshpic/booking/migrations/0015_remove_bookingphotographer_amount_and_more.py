# Generated by Django 5.0.2 on 2024-02-26 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0014_alter_bookingphotographer_booking_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookingphotographer",
            name="amount",
        ),
        migrations.AlterField(
            model_name="bookingphotographer",
            name="booking_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 26, 15, 14, 15, 681418)
            ),
        ),
    ]