# Generated by Django 2.2.7 on 2019-12-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_match_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='bracket_type',
            field=models.CharField(choices=[('SE', 'Single elimination')], default='SE', max_length=2),
        ),
        migrations.AddField(
            model_name='tournament',
            name='category',
            field=models.CharField(default='other', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]