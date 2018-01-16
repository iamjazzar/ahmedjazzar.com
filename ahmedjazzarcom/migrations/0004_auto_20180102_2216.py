# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0003_auto_20160111_1831'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MainPage',
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='latest_projects',
        ),
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.DeleteModel(
            name='LatestProject',
        ),
        migrations.DeleteModel(
            name='SideBar',
        ),
    ]
