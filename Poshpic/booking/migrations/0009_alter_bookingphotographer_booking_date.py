# Generated by Django 5.0.2 on 2024-02-17 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0008_alter_bookingphotographer_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookingphotographer",
            name="booking_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 17, 13, 59, 58, 873683)
            ),
        ),
    ]
