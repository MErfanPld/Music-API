from django.db import models
from django.contrib.auth import get_user_model
import time
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

User = get_user_model()


def upload_image(instance, filename):
    path = 'uploads/' + 'album/' + slugify(instance.title, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title) + '-' + filename
    return path + '/' + name


class Album(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_album')
    viewCount = models.IntegerField(default=0)
    likeCount = models.IntegerField(default=0)
    playCount = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    cover = models.ImageField(upload_to=upload_image, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('album', args=[self.slug])

    def __str__(self):
        return self.title
