# Generated by Django 3.0.2 on 2020-04-18 18:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0023_auto_20200416_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='occupation',
            fields=[
                ('occupation_id', models.AutoField(primary_key=True, serialize=False)),
                ('occupation', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 18, 18, 38, 1, 616118)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 18, 18, 38, 1, 617129)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 18, 18, 38, 1, 617891)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 18, 18, 38, 1, 618883)),
        ),
        migrations.CreateModel(
            name='crew',
            fields=[
                ('crew_id', models.AutoField(primary_key=True, serialize=False)),
                ('crew_name', models.CharField(max_length=50)),
                ('born_date', models.DateField()),
                ('born_place', models.CharField(max_length=20)),
                ('born_nation', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=500)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('more_info', models.URLField()),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.movie_content')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.occupation')),
                ('webseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.webseries_content')),
            ],
        ),
        migrations.CreateModel(
            name='cast',
            fields=[
                ('cast_id', models.AutoField(primary_key=True, serialize=False)),
                ('cast_name', models.CharField(max_length=50)),
                ('born_date', models.DateField()),
                ('born_place', models.CharField(max_length=20)),
                ('born_nation', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=500)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('more_info', models.URLField()),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.movie_content')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.occupation')),
                ('webseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.webseries_content')),
            ],
        ),
    ]
