# Generated by Django 5.0 on 2024-01-16 13:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_created_at_posthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='posthistory',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posthistory',
            name='like',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.like'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 19, 15, 20, 678269)),
        ),
        migrations.AlterField(
            model_name='posthistory',
            name='deleted_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 19, 15, 20, 678269)),
        ),
    ]