from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Playlist
from . import serializers

# Create your views here.

class PlaylistAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user ,status=True)
