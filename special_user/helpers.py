from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta

from special_user.models import Special


def check_special_expiration(user):
    if user.get_special():
        today = timezone.now()
        expiration = user.get_special().created_at + relativedelta(months=user.get_special().plan_music.time_months)

        if expiration >= today:
            return True

    return False


def show_expiration(user):
    expiration = user.get_special().created_at + relativedelta(months=user.get_special().plan_music.time_months)
    return datetime.datetime.fromgregorian(datetime=expiration)
