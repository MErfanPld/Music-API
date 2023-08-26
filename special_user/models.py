from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

# Create your models here.

User = get_user_model()


class PlanMusic(models.Model):
    title = models.CharField(max_length=225)
    time_months = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f'{self.title}, {self.price}'


class Special(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_music = models.ForeignKey(PlanMusic, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f'{self.user.get_username}, {self.plan_music},{self.expires_at}'
