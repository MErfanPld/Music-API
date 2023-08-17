from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = "acl"

router = SimpleRouter()
router.register('roles', views.RoleAPI)
router.register('permissions', views.PermissionsAPI)
router.register('role_user', views.UserRoleAPI)

urlpatterns = [
    path('', include(router.urls)),
]
