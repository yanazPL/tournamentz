# Generated by Django 2.2.7 on 2019-12-22 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='tournament',
            name='host',
            field=models.ManyToManyField(related_name='hosted_tournaments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='player',
            field=models.ManyToManyField(related_name='played_tournaments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournament',
            name='testy',
            field=models.ManyToManyField(to='core.Testy'),
        ),
    ]
