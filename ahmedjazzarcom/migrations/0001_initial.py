# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('about', models.TextField()),
                ('country', models.CharField(max_length=15)),
                ('country_image', models.ImageField(upload_to=b'/static/images')),
                ('logo', models.ImageField(upload_to=b'/static/images')),
                ('pattern', models.ImageField(upload_to=b'/static/images')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
