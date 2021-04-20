# Generated by Django 2.2.7 on 2020-05-10 16:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0015_auto_20200508_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_link',
            field=models.CharField(default='Some value', max_length=260),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='picture_link',
            field=models.CharField(default='Some value', max_length=260),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 16, 9, 24, 689493, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 16, 9, 24, 687689, tzinfo=utc)),
        ),
    ]
