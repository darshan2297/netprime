# Generated by Django 3.0.2 on 2020-05-04 10:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0067_auto_20200430_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='webseries_season_episode',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.language'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 10, 55, 37, 705371)),
        ),
        migrations.AlterField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 10, 55, 37, 712033)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 10, 55, 37, 708400)),
        ),
        migrations.AlterField(
            model_name='webseries_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 10, 55, 37, 712866)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 10, 55, 37, 710309)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 10, 55, 37, 711306)),
        ),
    ]
