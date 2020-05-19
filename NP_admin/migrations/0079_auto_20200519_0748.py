# Generated by Django 3.0.2 on 2020-05-19 07:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0078_auto_20200519_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 7, 48, 50, 112484)),
        ),
        migrations.AlterField(
            model_name='movie_link_detail',
            name='movie_download_link_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.movie_download_link'),
        ),
        migrations.AlterField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 7, 48, 50, 121041)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 7, 48, 50, 115465)),
        ),
        migrations.AlterField(
            model_name='webseries_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 7, 48, 50, 122025)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 7, 48, 50, 118477)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 7, 48, 50, 119200)),
        ),
    ]
