# Generated by Django 2.2.7 on 2020-05-10 16:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0017_auto_20200510_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 16, 29, 7, 541065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 16, 29, 7, 539557, tzinfo=utc)),
        ),
    ]
