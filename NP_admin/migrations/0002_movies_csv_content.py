# Generated by Django 3.0.2 on 2020-03-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NP_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies_csv_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_csv_file', models.FileField(blank=True, null=True, upload_to='movie_csv_file')),
            ],
        ),
    ]
