# Generated by Django 4.2.4 on 2023-08-18 20:31

from django.db import migrations, models
import playlist.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0004_music_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(upload_to=playlist.models.upload_image)),
                ('status', models.BooleanField(default=False)),
                ('musics', models.ManyToManyField(to='music.music')),
            ],
        ),
    ]