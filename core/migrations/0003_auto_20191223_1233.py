# Generated by Django 2.2.7 on 2019-12-23 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191222_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='testy',
        ),
        migrations.DeleteModel(
            name='Testy',
        ),
    ]