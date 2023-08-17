from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Music
from . import serializers


# Create your views here.

class MusicListCreateAPIView(ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer


class MusicRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Music.objects.filter(status=True)
    serializer_class = serializers.MusicSerializer
