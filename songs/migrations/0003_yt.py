# Generated by Django 4.0.6 on 2022-08-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_alter_song_artist_alter_song_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl_link', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
                ('search', models.CharField(max_length=50)),
            ],
        ),
    ]
