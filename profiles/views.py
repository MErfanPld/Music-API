from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from music.models import *
from album.models import *
from story.models import *
from playlist.models import *
from .serializers import *


# Create your views here.

User = get_user_model()

class ProfileUserViewAPI(APIView):
    def get(self, request, username,format=None):
        data = {}
        user = get_object_or_404(User, username=username)
        if user.role_code == "singer":
            data["musics"] = ProfileUserMusicSerializer(Music.objects.filter(
                singer__username=username, status=True), many=True).data
            data["albums"] = ProfileUserAlbumSerializer(
                Album.objects.filter(user__username=username,status=True), many=True).data
        else:
            data["story"] = ProfileUserStorySerializer(
                Story.objects.filter(user__username=username), many=True).data
            data["playlists"] = ProfileUserPlaylistSerializer(
                Playlist.objects.filter(user__username=username,status=True), many=True).data
        return Response({"data":data, "username":username}, status=status.HTTP_200_OK)
