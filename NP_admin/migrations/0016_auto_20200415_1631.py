# Generated by Django 3.0.2 on 2020-04-15 16:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0015_auto_20200413_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='webseries_content',
            fields=[
                ('webseries_id', models.AutoField(primary_key=True, serialize=False)),
                ('webseries_name', models.CharField(max_length=100)),
                ('duration_hours', models.IntegerField()),
                ('duration_minutes', models.IntegerField()),
                ('release_date', models.DateField()),
                ('language', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1500)),
                ('season', models.CharField(max_length=20)),
                ('episode', models.CharField(max_length=20)),
                ('webseries_poster', models.ImageField(blank=True, null=True, upload_to='webseries_poster')),
                ('webseries_session_poster', models.ImageField(blank=True, null=True, upload_to='webseries_session_poster')),
                ('webseries_episode_poster', models.ImageField(blank=True, null=True, upload_to='webseries_episode_poster')),
                ('webseries_trailer_thumbnail', models.ImageField(null=True, upload_to='webseries_trailers_thumbnail')),
                ('webseries_trailer_576p', models.FileField(null=True, upload_to='webseries_trailers_576p')),
                ('webseries_trailer_720p', models.FileField(null=True, upload_to='webseries_trailers_720p')),
                ('webseries_trailer_1080p', models.FileField(null=True, upload_to='webseries_trailers_1080p')),
                ('webseries_thumbnail', models.ImageField(null=True, upload_to='webseries_thumbnail')),
                ('webseries_576p', models.FileField(null=True, upload_to='webseries_576p')),
                ('webseries_720p', models.FileField(null=True, upload_to='webseries_720p')),
                ('webseries_1080p', models.FileField(null=True, upload_to='webseries_1080p')),
                ('webseries_bgimage', models.ImageField(null=True, upload_to='webseries_background')),
                ('created_date', models.DateField(default=datetime.datetime(2020, 4, 15, 16, 31, 51, 405288))),
                ('main_catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.main_catagory')),
                ('sub_catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.sub_catagory')),
                ('type_catagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NP_admin.type_catagory')),
            ],
        ),
        migrations.RemoveField(
            model_name='web_sub_catagory',
            name='main_catagory',
        ),
        migrations.RemoveField(
            model_name='web_type_catagory',
            name='main_catagory',
        ),
        migrations.RemoveField(
            model_name='web_type_catagory',
            name='sub_catagory',
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 16, 31, 51, 404100)),
        ),
        migrations.DeleteModel(
            name='web_main_catagory',
        ),
        migrations.DeleteModel(
            name='web_sub_catagory',
        ),
        migrations.DeleteModel(
            name='web_type_catagory',
        ),
    ]
