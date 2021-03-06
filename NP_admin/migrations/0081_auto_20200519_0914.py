# Generated by Django 3.0.2 on 2020-05-19 09:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0080_auto_20200519_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='webseries_download_link',
            name='season',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='webseries_download_link',
            name='season_release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 9, 14, 1, 369120)),
        ),
        migrations.AlterField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 9, 14, 1, 378311)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 9, 14, 1, 372189)),
        ),
        migrations.AlterField(
            model_name='webseries_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 9, 14, 1, 379153)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 9, 14, 1, 375180)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 9, 14, 1, 375913)),
        ),
        migrations.CreateModel(
            name='webseries_link_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=100)),
                ('episode', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
                ('webseries_download_link_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.webseries_download_link')),
            ],
        ),
    ]
