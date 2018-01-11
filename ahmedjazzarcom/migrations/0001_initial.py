# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interest', models.CharField(max_length=15)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('logo', models.ImageField(upload_to=b'images')),
                ('country', models.CharField(max_length=15)),
                ('work_location', models.CharField(max_length=25)),
                ('organization', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=50)),
                ('organization_link', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('github_username', models.CharField(max_length=25)),
                ('twitter_username', models.CharField(max_length=25)),
                ('linkedin_username', models.CharField(max_length=25)),
                ('facebook_username', models.CharField(max_length=25)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about', models.TextField()),
                ('birth_date', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('interests', models.ForeignKey(
                    to='ahmedjazzarcom.Interest',
                    on_delete=models.CASCADE
                )),
                ('latest_projects', models.ForeignKey(
                    to='ahmedjazzarcom.LatestProject',
                    on_delete=models.CASCADE
                )),
            ],
        ),
    ]
