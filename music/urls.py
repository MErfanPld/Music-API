from django.urls import path

from . import views

app_name = "music"

urlpatterns = [
    path('', views.MusicListAPIView.as_view(), name="music_list"),
    path('', views.MusicCreateAPIView.as_view(), name="music_create"),
    path('<int:pk>/', views.MusicRetrieveAPIView.as_view(), name="music_retrieve"),
    path('<int:pk>/', views.MusicUpdateAPIView.as_view(), name="music_update"),
    path('<int:pk>/', views.MusicDestroyAPIView.as_view(), name="music_delete"),
]
