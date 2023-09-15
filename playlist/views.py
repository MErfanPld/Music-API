from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .models import Playlist
from . import serializers

# Create your views here.

class PlaylistAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PlaylistSerializer
    search_fields = ["title","slug"]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user ,status=True)
