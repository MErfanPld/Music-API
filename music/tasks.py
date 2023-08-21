from celery import shared_task
from config.celery import celery_app
from celery import shared_task

from .models import Music
from django.utils import timezone
from datetime import timedelta, datetime
import pytz


@shared_task()
def upload_music_token():
    if Music.created_at != datetime.now():
        Music.status = False
    else:
        return Music.objects.create()
    print("Created Music ...")
