from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from music.models import *
from album.models import *
from story.models import *
from .serializers import *

# Create your views here.


class ProfileUserMusicViewAPI(ListAPIView):
    serializer_class = ProfileUserMusicSerializer

    def get_queryset(self):
        return Music.objects.filter(singer=self.request.user, status=True)


class ProfileUserAlbumViewAPI(ListAPIView):
    serializer_class = ProfileUserAlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user, status=True)


class ProfileUserStoryViewAPI(ListAPIView):
    serializer_class = ProfileUserStorySerializer

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user)
