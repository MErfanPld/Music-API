from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from acl.mixins import *
from .models import Music
from . import serializers
from acl.rest_mixin import *

# Create your views here.

class MusicListAPIView(ListAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_list']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicCreateAPIView(PermissionMixin, CreateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_create']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicRetrieveAPIView(PermissionMixin, RetrieveAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_detail']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicUpdateAPIView(PermissionMixin, UpdateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_edit']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicDestroyAPIView(PermissionMixin, DestroyAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_delete']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer
