from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = "special"

router = SimpleRouter()
router.register('plan/music', views.PlanMusicAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.SpecialListAPIView.as_view(), name="special_list"),
    path('create/', views.SpecialCreateAPIView.as_view(), name="special_create"),
    path('delete/', views.SpecialDeleteAPIView.as_view(), name="special_delete"),
]
