# Generated by Django 2.0.7 on 2018-08-08 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0002_auto_20180808_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 5, 54, 36, 746487, tzinfo=utc)),
        ),
    ]
