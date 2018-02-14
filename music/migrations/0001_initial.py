# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(default=b'Male', max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('address', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(default=b'Pop', max_length=25, choices=[(b'Pop', b'Pop'), (b'Reggae', b'Reggae'), (b'Country', b'Country'), (b'Jazz', b'Jazz'), (b'Hip Hop', b'Hip Hop'), (b'Rock', b'Rock'), (b'R&B and Souls', b'R&B and Souls'), (b'Dangdut', b'Dangdut')])),
                ('singer', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
