# Generated by Django 3.0.2 on 2020-05-17 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0075_auto_20200517_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 14, 44, 39, 781189)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 14, 44, 39, 781286), null=True),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='member_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 14, 44, 39, 781159)),
        ),
    ]