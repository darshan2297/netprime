# Generated by Django 3.0.2 on 2020-04-26 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0057_auto_20200426_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 2, 22, 48, 566044)),
        ),
        migrations.AlterField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 2, 22, 48, 571710)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 2, 22, 48, 568256)),
        ),
        migrations.AlterField(
            model_name='webseries_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 2, 22, 48, 572545)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 2, 22, 48, 570299)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 2, 22, 48, 571017)),
        ),
    ]
