# Generated by Django 3.0.2 on 2020-04-21 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0037_auto_20200419_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 10, 40, 3, 385150)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 10, 40, 3, 385175), null=True),
        ),
    ]
