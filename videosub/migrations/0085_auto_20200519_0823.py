# Generated by Django 3.0.2 on 2020-05-19 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0084_auto_20200519_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 8, 23, 1, 185416)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 8, 23, 1, 185453), null=True),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='member_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 8, 23, 1, 185371)),
        ),
    ]
