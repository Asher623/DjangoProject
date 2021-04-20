# Generated by Django 2.2.7 on 2020-05-02 19:12

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simple_app', '0004_auto_20200427_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 2, 19, 12, 10, 188840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2020, 5, 2, 19, 12, 10, 187975, tzinfo=utc)),
        ),
    ]
