from django.urls import path

from . import views

app_name = "album"

urlpatterns = [
    path('', views.AlbumListAPIView.as_view(), name="album_list"),
    path('create/', views.AlbumCreateAPIView.as_view(), name="album_create"),
    path('<int:pk>/', views.AlbumRetrieveAPIView.as_view(), name="album_retrieve"),
    path('update/<int:pk>/', views.AlbumUpdateAPIView.as_view(), name="album_update"),
    path('delete/<int:pk>/', views.AlbumDestroyAPIView.as_view(), name="album_delete"),
]
