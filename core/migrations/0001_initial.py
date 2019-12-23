# Generated by Django 3.0.1 on 2019-12-22 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('host', models.ManyToManyField(related_name='hosts', to=settings.AUTH_USER_MODEL)),
                ('player', models.ManyToManyField(related_name='players', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]