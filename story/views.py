from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Story
from . import serializers


# Create your views here.

class StoryListAPIView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer


class StoryCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer


class StoryRetrieveAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer


class StoryUpdateAPIView(UpdateAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer


class StoryDestroyAPIView(DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer
