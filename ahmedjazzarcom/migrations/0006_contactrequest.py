# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0005_socialaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('message', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
