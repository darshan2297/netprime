# Generated by Django 3.0.2 on 2020-04-19 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0027_auto_20200419_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='occupation',
        ),
        migrations.AddField(
            model_name='cast',
            name='occupation',
            field=models.ManyToManyField(blank=True, null=True, to='NP_admin.occupation'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 10, 32, 32, 982878)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 10, 32, 32, 984428)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 10, 32, 32, 985316)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 10, 32, 32, 986137)),
        ),
    ]
