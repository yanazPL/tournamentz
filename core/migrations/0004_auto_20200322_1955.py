# Generated by Django 3.0.1 on 2020-03-22 19:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200322_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 19, 55, 53, 992023, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='core.Tournament'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 19, 55, 53, 990604, tzinfo=utc)),
        ),
    ]
