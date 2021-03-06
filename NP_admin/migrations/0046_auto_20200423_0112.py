# Generated by Django 3.0.2 on 2020-04-23 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0045_auto_20200423_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 12, 11, 589253)),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 12, 11, 595106)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 12, 11, 591631)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 12, 11, 593479)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 12, 11, 594421)),
        ),
    ]
