# Generated by Django 3.0.1 on 2020-03-22 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='stats',
        ),
        migrations.AlterField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 16, 55, 28, 844621, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 16, 55, 28, 843159, tzinfo=utc)),
        ),
    ]
