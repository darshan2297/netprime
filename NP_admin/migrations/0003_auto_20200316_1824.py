# Generated by Django 3.0.2 on 2020-03-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0002_movies_csv_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_csv_content',
            name='movie_csv_file',
            field=models.FileField(default=1, upload_to='movie_csv_file'),
            preserve_default=False,
        ),
    ]
