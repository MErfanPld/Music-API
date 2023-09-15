from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.response import Response
from acl.mixins import *
from .models import Music
from . import serializers
from acl.rest_mixin import *

# Create your views here.


class MusicListAPIView(ListAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_list']
    search_fields = ["title","slug"]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicCreateAPIView(CreateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_create']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


# class MusicRetrieveAPIView(RetrieveAPIView):
#     permission_classes = [RestPermissionMixin]
#     permissions = ['music_detail']
#     queryset = Music.objects.filter(status=True)
#     serializer_class = serializers.MusicSerializer

class MusicRetrieveAPIView(APIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_detail']
    serializer_class = serializers.MusicSerializer

    def dispatch(self, request, pk, format=None):
        if Music.is_special_music and self.request.user.get_special:
            music = Music.objects.filter(is_special_music=True, pk=pk)
            return Response(music,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MusicUpdateAPIView(UpdateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_edit']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicDestroyAPIView(DestroyAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['music_delete']
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicSpecialAPIView(APIView):
    def get(self, resquest):
        pass
