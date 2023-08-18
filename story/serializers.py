from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ["id", "user", "file"]
