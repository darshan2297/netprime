# Generated by Django 3.0.2 on 2020-04-22 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0040_auto_20200421_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 12, 8, 12, 101934)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 12, 8, 12, 101961), null=True),
        ),
    ]
