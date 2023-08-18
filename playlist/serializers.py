from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "title", "slug", "image", "musics", "status"]
