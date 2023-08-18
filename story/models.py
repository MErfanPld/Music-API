from django.db import models
from django.contrib.auth import get_user_model
import time
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

User = get_user_model()


def upload_story_file(instance, filename):
    path = 'uploads/' + 'story/' + slugify(instance.user, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.user) + '-' + filename
    return path + '/' + name


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_story_file)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

