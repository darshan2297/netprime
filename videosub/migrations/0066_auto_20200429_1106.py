# Generated by Django 3.0.2 on 2020-04-29 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0065_auto_20200428_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 11, 6, 52, 536923)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 11, 6, 52, 536949), null=True),
        ),
    ]
