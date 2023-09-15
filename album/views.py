from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import filters
from acl.mixins import *
from .models import Album
from . import serializers
from acl.rest_mixin import *

# Create your views here.


class AlbumListAPIView(ListAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['album_list']
    search_fields = ["title","slug"]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    queryset = Album.objects.filter(status=True)
    serializer_class = serializers.AlbumSerializer


class AlbumCreateAPIView(CreateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['album_create']
    queryset = Album.objects.filter(status=True)
    serializer_class = serializers.AlbumSerializer


class AlbumRetrieveAPIView(RetrieveAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['album_detail']
    queryset = Album.objects.filter(status=True)
    serializer_class = serializers.AlbumSerializer


class AlbumUpdateAPIView(UpdateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['album_edit']
    queryset = Album.objects.filter(status=True)
    serializer_class = serializers.AlbumSerializer


class AlbumDestroyAPIView(DestroyAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['album_delete']
    queryset = Album.objects.filter(status=True)
    serializer_class = serializers.AlbumSerializer
