from typing import NamedTuple

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Measurement(models.Model):
    class Health(models.TextChoices):
        EXCELLENT = 'EXCELLENT', 'Excellent'
        GOOD = 'GOOD', 'Good'
        BAD = 'BAD', 'Bad'

    user = models.ForeignKey(
        get_user_model(),
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        verbose_name='User',
    )
    day = models.DateField(
        default=timezone.now,
        verbose_name='Measurement day',
    )
    time = models.TimeField(
        default=timezone.now,
        verbose_name='Measurement time',
    )
    temperature = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name='Temperature (Celsius)',
    )
    health = models.CharField(
        max_length=9,
        choices=Health.choices,
        default=Health.EXCELLENT,
        verbose_name='Health',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description',
    )
    is_bout = models.BooleanField(
        default=False,
        verbose_name='High blood pressure bout',
    )

    class Meta:
        db_table = 'measurement'
        verbose_name = 'measurement'
        verbose_name_plural = 'measurements'

    def __str__(self) -> str:
        return str(self.day)

    @property
    def day_string(self) -> str:
        return self.day.strftime('%d-%m-%Y') # noqa

    @property
    def time_string(self) -> str:
        time = self.time
        hours, minutes, _ = str(time).split(':')
        return f'{hours}:{minutes}'

    class Hand(NamedTuple):
        blood_pressure: str
        pulse: str

    @classmethod
    def hand_data(cls, hand) -> Hand:
        return cls.Hand(
            blood_pressure=f'{hand.systolic}/{hand.diastolic}',
            pulse=hand.pulse,
        ) if hand else '-'
