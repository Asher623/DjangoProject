# Generated by Django 2.2.7 on 2020-05-10 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0019_auto_20200510_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 17, 7, 45, 790788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 10, 17, 7, 45, 789242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='picture_link',
            field=models.URLField(blank=True),
        ),
    ]