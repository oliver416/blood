import pytz
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TIMEZONES = [(zone, zone) for zone in pytz.all_timezones]

    timezone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=TIMEZONES,
        verbose_name='Current timezone',
    )
