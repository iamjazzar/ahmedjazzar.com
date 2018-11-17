from django.db import migrations
import martor.models


class Migration(migrations.Migration):
    dependencies = [
        ('ahmedjazzarcom', '0022_slider_inverse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=martor.models.MartorField(),
        ),
    ]

