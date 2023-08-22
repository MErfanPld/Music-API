from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from music.models import Music

User = get_user_model()


class Like_And_DisLike(models.Model):
    user = models.ForeignKey(
        to=User, related_name='likes_and_dislikes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(Music, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()
    types_options = (('like', 'Like'), ('dislike', 'DisLike'))
    type = models.CharField(max_length=10, choices=types_options)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
