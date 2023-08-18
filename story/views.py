from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .models import Story
from . import serializers


# Create your views here.

class StoryListAPIView(ListAPIView):
    serializer_class = serializers.StorySerializer
    queryset = Story.objects.all()


class StoryCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer


class StoryRetrieveAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer


class StoryUpdateAPIView(UpdateAPIView):
    serializer_class = serializers.StorySerializer

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user)


class StoryDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.StorySerializer

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user)
