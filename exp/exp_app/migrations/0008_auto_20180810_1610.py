# Generated by Django 2.0.7 on 2018-08-10 10:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0007_auto_20180809_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 10, 40, 39, 430224, tzinfo=utc)),
        ),
    ]
