from rest_framework import serializers
from django.contrib.auth import authenticate
from music.models import *
from album.models import *
from story.models import *


class ProfileUserMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["id", "title", "slug", "singer", "album", "audio_file",
                  "audio_link", "status", "cover", "viewCount", "likeCount", "playCount"]


class ProfileUserAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title", "slug", "status",
                  "cover", "viewCount", "likeCount", "playCount"]


class ProfileUserStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ["id", "user", "file"]
