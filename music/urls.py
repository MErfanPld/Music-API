from django.urls import path

from . import views

app_name = "music"

urlpatterns = [
    path('', views.MusicListCreateAPIView.as_view(), name="music_list_create"),
    path('<int:pk>/', views.MusicRetrieveUpdateDestroyAPIView.as_view(),
         name="music_detail_update_delete"),
]
