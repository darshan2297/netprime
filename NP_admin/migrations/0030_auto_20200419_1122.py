# Generated by Django 3.0.2 on 2020-04-19 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0029_auto_20200419_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='occupation',
        ),
        migrations.AddField(
            model_name='crew',
            name='occupation',
            field=models.ManyToManyField(blank=True, null=True, to='NP_admin.occupation'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 11, 22, 11, 358574)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 11, 22, 11, 360764)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 11, 22, 11, 361542)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 11, 22, 11, 362271)),
        ),
    ]
