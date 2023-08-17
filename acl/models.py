from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Role(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(
                            max_length=255, unique=True)
    description = models.TextField(
        max_length=500, null=True, blank=True)
    permissions = models.ManyToManyField(
        to='Permission', related_name='role', blank=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def permissions_list(self):
        return list(self.permissions.values_list('code', flat=True))


class Permission(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(
                            max_length=255, unique=True)
    description = models.TextField(
        max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.name}-{self.code}"


class UserRole(models.Model):
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE,
                             related_name='users', null=True, blank=True)
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, related_name='role')

    def __str__(self):
        return f"{self.user}-{self.role.name}"

    @property
    def role_name(self):
        if self.role:
            return self.role.name
        return 'user'
