from django.contrib import admin

from .models import Measurement, RightHand, LeftHand


class RightHandInlineAdmin(admin.StackedInline):
    model = RightHand


class LeftHandInlineAdmin(admin.StackedInline):
    model = LeftHand


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    inlines = (
        RightHandInlineAdmin,
        LeftHandInlineAdmin,
    )
