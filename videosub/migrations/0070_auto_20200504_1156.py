# Generated by Django 3.0.2 on 2020-05-04 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosub', '0069_auto_20200504_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_record',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 11, 56, 54, 746514)),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 11, 56, 54, 746527), null=True),
        ),
        migrations.AlterField(
            model_name='member_record',
            name='member_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 11, 56, 54, 746472)),
        ),
    ]