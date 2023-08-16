from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
import time
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from accounts.managers import UserManager

# Create your models here.

def upload_image(instance, filename):
    path = 'uploads/' + 'users/' + slugify(instance.username, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.username) + '-' + filename
    return path + '/' + name


class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=30, unique=True)
    email = models.EmailField(('email'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    phoneNumber = models.CharField(('phone number'), max_length=11, blank=True)
    email_verified_at = models.DateTimeField(verbose_name=('email_verified_at') , null=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    last_login = models.DateTimeField(('last login'), auto_now=True)
    is_superuser = models.BooleanField(('is superuser'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('is staff'), default=False)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    level = models.CharField(('level') , default='user' , max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' , 'password']

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
