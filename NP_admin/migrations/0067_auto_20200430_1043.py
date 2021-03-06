# Generated by Django 3.0.2 on 2020-04-30 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0066_auto_20200429_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='occupation',
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast_profile',
            field=models.ImageField(blank=True, null=True, upload_to='cast_profile'),
        ),
        migrations.AlterField(
            model_name='crew',
            name='crew_profile',
            field=models.ImageField(blank=True, null=True, upload_to='crew_profile'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='cast',
            field=models.ManyToManyField(blank=True, to='NP_admin.cast'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 10, 43, 57, 162677)),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='crew',
            field=models.ManyToManyField(blank=True, to='NP_admin.crew'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='movie_bgimage',
            field=models.ImageField(blank=True, null=True, upload_to='movie_background'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='movie_trailer_720p',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='movie_trailers_720p'),
        ),
        migrations.AlterField(
            model_name='movie_content',
            name='movie_trailer_thumbnail',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='movie_trailers_thumbnail'),
        ),
        migrations.AlterField(
            model_name='movie_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 10, 43, 57, 173266)),
        ),
        migrations.AlterField(
            model_name='multiple_audio_movies',
            name='movie_720p',
            field=models.FileField(blank=True, null=True, upload_to='movie_720p'),
        ),
        migrations.AlterField(
            model_name='multiple_audio_movies',
            name='movie_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='movie_thumbnail'),
        ),
        migrations.AlterField(
            model_name='sub_catagory',
            name='sub_cat_image',
            field=models.ImageField(blank=True, null=True, upload_to='sub_cat_image'),
        ),
        migrations.AlterField(
            model_name='type_catagory',
            name='type_cat_image',
            field=models.ImageField(blank=True, null=True, upload_to='type_cat_image'),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 10, 43, 57, 167569)),
        ),
        migrations.AlterField(
            model_name='webseries_content',
            name='webseries_bgimage',
            field=models.ImageField(blank=True, null=True, upload_to='webseries_background'),
        ),
        migrations.AlterField(
            model_name='webseries_review',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 10, 43, 57, 174681)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 10, 43, 57, 170637)),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='webseries_trailer_720p',
            field=models.FileField(blank=True, null=True, upload_to='webseries_trailers_720p'),
        ),
        migrations.AlterField(
            model_name='webseries_season',
            name='webseries_trailer_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='webseries_trailers_thumbnail'),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 10, 43, 57, 172055)),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='webseries_720p',
            field=models.FileField(blank=True, null=True, upload_to='webseries_720p'),
        ),
        migrations.AlterField(
            model_name='webseries_season_episode',
            name='webseries_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='webseries_thumbnail'),
        ),
        migrations.DeleteModel(
            name='occupation',
        ),
    ]
