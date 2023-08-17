from django.db import models
from django.contrib.auth import get_user_model
import time
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

User = get_user_model()


def upload_image(instance, filename):
    path = 'uploads/' + 'music/' + slugify(instance.singer, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.singer) + '-' + filename
    return path + '/' + name


def upload_audio_file(instance, filename):
    path = 'uploads/' + 'music/' + 'audio' +slugify(instance.singer, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.singer) + '-' + filename
    return path + '/' + name


class Music(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50)
    singer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='singer_music')
    audio_file = models.FileField(
        upload_to=upload_audio_file, blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    viewCount = models.IntegerField(default=0)
    likeCount = models.IntegerField(default=0)
    playCount = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    cover = models.ImageField(upload_to=upload_image, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('music', args=[self.slug])

    def __str__(self):
        return self.title
