from django.db import models
import time
from django.urls import reverse
from django.utils.text import slugify

from music.models import Music

# Create your models here.


def upload_image(instance, filename):
    path = 'uploads/' + 'playlist/' + \
        slugify(instance.title, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title) + '-' + filename
    return path + '/' + name


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to=upload_image)
    musics = models.ManyToManyField(Music)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('playlist', args=[self.slug])

    def __str__(self):
        return self.title
