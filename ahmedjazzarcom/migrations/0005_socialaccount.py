# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0004_auto_20180102_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=55)),
                ('link', models.URLField()),
                ('css_class', models.CharField(max_length=128, blank=True, null=True)),
            ],
        ),
    ]
