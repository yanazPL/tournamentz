# Generated by Django 3.0.1 on 2019-12-23 17:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191223_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 23, 17, 11, 16, 112372, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 23, 17, 11, 16, 110885, tzinfo=utc)),
        ),
    ]
