# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('href', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='headerdata',
            name='country_image',
            field=models.ImageField(upload_to=b'static/images'),
        ),
        migrations.AlterField(
            model_name='headerdata',
            name='logo',
            field=models.ImageField(upload_to=b'static/images'),
        ),
        migrations.AlterField(
            model_name='headerdata',
            name='pattern',
            field=models.ImageField(upload_to=b'static/images'),
        ),
    ]
