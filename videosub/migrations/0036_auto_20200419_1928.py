# Generated by Django 3.0.2 on 2020-04-19 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0035_auto_20200419_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 19, 28, 41, 621922)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 19, 28, 41, 621949), null=True),
        ),
    ]
