# Generated by Django 5.0 on 2024-01-18 18:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_alter_comment_created_at_alter_like_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 23, 40, 41, 702009)),
        ),
        migrations.AlterField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 23, 40, 41, 702009)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 23, 40, 41, 702009)),
        ),
        migrations.AlterField(
            model_name='posthistory',
            name='deleted_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 23, 40, 41, 702009)),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(default=datetime.datetime(2024, 1, 18, 23, 40, 41, 703007))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]