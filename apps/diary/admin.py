from django.contrib import admin

from .models import Measurement, RightHand, LeftHand


class RightHandInlineAdmin(admin.StackedInline):
    model = RightHand


class LeftHandInlineAdmin(admin.StackedInline):
    model = LeftHand


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'day_',
        'time_',
        'left_hand_',
        'right_hand_',
        'temperature_',
        'health',
        'is_bout_',
        'description',
    )
    list_display_links = (
        'day_',
    )

    @admin.display(description='Day')
    def day_(self, measurement: Measurement) -> str:
        return measurement.day.strftime('%d-%m-%Y')

    @admin.display(description='Local time')
    def time_(self, measurement: Measurement) -> str:
        time = measurement.time
        hours, minutes, _ = str(time).split(':')
        return f'{hours}:{minutes}'

    @admin.display(description=f'T\N{DEGREE SIGN}C')
    def temperature_(self, measurement: Measurement) -> str:
        return measurement.temperature

    @admin.display(description='Bout', boolean=True)
    def is_bout_(self, measurement: Measurement) -> bool:
        return measurement.is_bout

    @admin.display(description='Right hand')
    def right_hand_(self, measurement: Measurement) -> str:
        hand = measurement.right_hand # noqa
        return f'{hand.systolic}/{hand.diastolic}/{hand.pulse}'

    @admin.display(description='Left hand')
    def left_hand_(self, measurement: Measurement) -> str:
        hand = measurement.left_hand # noqa
        return f'{hand.systolic}/{hand.diastolic}/{hand.pulse}'

    def save_model(self, request, obj, form, change):
        if not getattr(obj, 'user', None):
            obj.user = request.user

        super().save_model(request, obj, form, change)

    inlines = (
        RightHandInlineAdmin,
        LeftHandInlineAdmin,
    )
