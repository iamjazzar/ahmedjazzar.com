# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0002_auto_20160111_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebar',
            name='interests',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='interests',
            field=models.ManyToManyField(to='ahmedjazzarcom.Interest'),
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='latest_projects',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='latest_projects',
            field=models.ManyToManyField(to='ahmedjazzarcom.LatestProject'),
        ),
    ]
