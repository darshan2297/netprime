# Generated by Django 3.0.2 on 2020-03-16 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0002_auto_20200316_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 18, 16, 42, 353965), null=True),
        ),
    ]
