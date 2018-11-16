from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0021_auto_20180119_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='inverse',
            field=models.BooleanField(default=False),
        ),
    ]
