# Generated by Django 2.2.7 on 2020-05-08 21:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0014_auto_20200507_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 8, 21, 52, 16, 874509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 8, 21, 52, 16, 872993, tzinfo=utc)),
        ),
    ]
