from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title", "slug", "status",
                  "cover", "viewCount", "likeCount", "playCount"]
