# Generated by Django 3.0.2 on 2020-05-19 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0095_auto_20200519_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 9, 31, 33, 556771)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 9, 31, 33, 556784), null=True),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='member_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 9, 31, 33, 556741)),
        ),
    ]
