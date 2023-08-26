from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["id", "title", "slug", "singer", "album", "audio_file",
                  "audio_link", "is_special_music", "status", "cover", "viewCount", "likeCount", "playCount"]
