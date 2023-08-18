from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "playlist"

router = DefaultRouter()
router.register('', views.PlaylistAPIView, basename="playlist_view")

urlpatterns = [
    path('', include(router.urls))
]
