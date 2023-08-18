from django.urls import path

from . import views

app_name = "story"

urlpatterns = [
    path('', views.StoryListAPIView.as_view(), name="story_list"),
    path('', views.StoryCreateAPIView.as_view(), name="story_create"),
    path('<int:pk>/', views.StoryRetrieveAPIView.as_view(), name="story_retrieve"),
    path('<int:pk>/', views.StoryUpdateAPIView.as_view(), name="story_update"),
    path('<int:pk>/', views.StoryDestroyAPIView.as_view(), name="story_delete"),
]
