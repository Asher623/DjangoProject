# Generated by Django 2.2.7 on 2020-04-27 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0003_auto_20200426_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 4, 27, 22, 12, 22, 906150, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 4, 27, 22, 12, 22, 905789, tzinfo=utc)),
        ),
    ]
