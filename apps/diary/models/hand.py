from django.db import models
from django.core.validators import MaxValueValidator


class Hand(models.Model):
    systolic = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(500),
        ],
        verbose_name='Systolic (high) blood pressure',
    )
    diastolic = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(500),
        ],
        verbose_name='Diastolic (high) blood pressure',
    )
    pulse = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(500),
        ],
        verbose_name='Pulse',
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return ''


class RightHand(Hand):
    measurement = models.OneToOneField(
        'diary.Measurement',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='right_hand',
        verbose_name='Measurement',
    )

    class Meta:
        db_table = 'right_hand'
        verbose_name = 'right hand'
        verbose_name_plural = 'right hands'


class LeftHand(Hand):
    measurement = models.OneToOneField(
        'diary.Measurement',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='left_hand',
        verbose_name='Measurement',
    )

    class Meta:
        db_table = 'left_hand'
        verbose_name = 'left hand'
        verbose_name_plural = 'left hands'
