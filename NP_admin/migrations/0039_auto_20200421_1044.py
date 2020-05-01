# Generated by Django 3.0.2 on 2020-04-21 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0038_auto_20200421_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 10, 44, 5, 212272)),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 10, 44, 5, 204989)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 10, 44, 5, 207359)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 10, 44, 5, 209231)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 10, 44, 5, 210160)),
        ),
    ]
