# Generated by Django 3.0.2 on 2020-04-13 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0015_auto_20200320_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 11, 38, 14, 372460)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 11, 38, 14, 372487), null=True),
        ),
    ]
