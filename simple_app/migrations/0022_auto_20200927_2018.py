# Generated by Django 3.1 on 2020-09-27 20:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0021_auto_20200927_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='picture_link',
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 9, 27, 20, 18, 58, 429321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 9, 27, 20, 18, 58, 427841, tzinfo=utc)),
        ),
    ]
