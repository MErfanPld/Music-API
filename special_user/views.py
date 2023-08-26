from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from acl.mixins import *
from .models import Special, PlanMusic
from . import serializers

# Create your views here.


class PlanMusicAPI(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = PlanMusic.objects.all()
    serializer_class = serializers.PlanMusicSerializer


class SpecialListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.SpecialSerializer

    def get_queryset(self):
        return Special.objects.filter(user=self.request.user)


class SpecialCreateAPIView(CreateAPIView):
    serializer_class = serializers.SpecialSerializer

    def get_queryset(self):
        return Special.objects.filter(user=self.request.user)

class SpecialDeleteAPIView(DestroyAPIView):
    serializer_class = serializers.SpecialSerializer
    queryset = Special.objects.all
