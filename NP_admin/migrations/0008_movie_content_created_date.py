# Generated by Django 3.0.2 on 2020-03-20 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0007_auto_20200319_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.date(2020, 3, 20)),
        ),
    ]
