from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from acl.mixins import *
from .models import Music
from . import serializers


# Create your views here.

class MusicListAPIView(PermissionMixin, ListAPIView):
    permissions = ['music_list']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicCreateAPIView(PermissionMixin, CreateAPIView):
    permissions = ['music_create']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicRetrieveAPIView(PermissionMixin, RetrieveAPIView):
    permissions = ['music_detail']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicUpdateAPIView(PermissionMixin, UpdateAPIView):
    permissions = ['music_edit']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicDestroyAPIView(PermissionMixin, DestroyAPIView):
    permissions = ['music_delete']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer
