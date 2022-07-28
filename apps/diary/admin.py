from django.contrib import admin
from django.http import HttpResponse

from .services import PDFCreationService
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
    actions = [
        'export_to_pdf',
    ]

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

    @admin.action(description='Export to PDF')
    def export_to_pdf(self, request, queryset) -> HttpResponse:
        pdf = PDFCreationService.create_pdf(request, queryset)
        headers = {
            'Content-Disposition': f'attachment; '
                                   f'filename="{PDFCreationService.PDF_NAME}"',
            'Content-Length': len(pdf),
        }
        return HttpResponse(
            pdf,
            content_type='application/pdf',
            headers=headers,
        )

    def has_delete_permission(self, request, obj=None):
        return False

    inlines = (
        RightHandInlineAdmin,
        LeftHandInlineAdmin,
    )
