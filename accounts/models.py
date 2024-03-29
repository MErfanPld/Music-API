from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
import time
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from accounts.managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from acl.permissions import PERMISSIONS

# Create your models here.


def upload_image(instance, filename):
    path = 'uploads/' + 'users/' + \
        slugify(instance.username, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.username) + '-' + filename
    return path + '/' + name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=30, unique=True)
    email = models.EmailField(('email'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    phoneNumber = models.CharField(('phone number'), max_length=11, blank=True)
    email_verified_at = models.DateTimeField(
        verbose_name=('email_verified_at'), null=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    last_login = models.DateTimeField(('last login'), auto_now=True)
    is_superuser = models.BooleanField(('is superuser'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('is staff'), default=False)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    level = models.CharField(('level'), default='user', max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f'{self.username}, {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.username

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def user_role(self):
        return self.role if hasattr(self, 'role') else None

    @property
    def role_code(self):
        if hasattr(self, 'role') and self.role.role:
            return self.role.role.code
        else:
            return None

    @property
    def role_code_display(self):
        return self.role.role_name if hasattr(self, 'role') else 'user'

    @property
    def has_role(self):
        if hasattr(self, 'role'):
            return True
        return False

    def change_role(self, role):
        from acl.models import UserRole
        user_role, _ = UserRole.objects.get_or_create(user=self)
        user_role.role = role
        user_role.save()
        return True

    @property
    def permissions(self):
        if self.is_superuser:
            return PERMISSIONS
        else:
            try:
                return self.role.role.permissions_list
            except:
                return []

    def check_has_permission(self, permission):
        if permission in self.permissions:
            return True
        return False

    def get_special(self):
        return self.special.filter(status=True).first()
