from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path('music/', views.ProfileUserMusicViewAPI.as_view(), name="profile_music_user"),
    path('album/', views.ProfileUserAlbumViewAPI.as_view(), name="profile_album_user"),
    path('story/', views.ProfileUserStoryViewAPI.as_view(), name="profile_story_user"),
]
