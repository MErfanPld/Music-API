from celery import shared_task
from config.celery import celery_app

from rest_framework_simplejwt.tokens import OutstandingToken
from datetime import timedelta, datetime, date
import pytz


@shared_task()
def expires_token():
    if OutstandingToken.expires_at != datetime.now():
        OutstandingToken.objects.all().delete()
        print("Done Expires Token ...")
