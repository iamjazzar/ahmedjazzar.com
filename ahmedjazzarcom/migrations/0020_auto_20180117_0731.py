# Generated by Django 2.0.1 on 2018-01-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0019_slider_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='order',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='slider',
            unique_together={('page', 'order')},
        ),
    ]
