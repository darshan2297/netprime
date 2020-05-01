# Generated by Django 3.0.2 on 2020-04-15 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0016_auto_20200415_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='webseries_content',
            name='season_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 16, 37, 17, 43271)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 16, 37, 17, 44524)),
        ),
    ]
