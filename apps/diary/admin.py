from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings
from rangefilter.filters import DateRangeFilter
from modeltranslation.admin import TranslationAdmin

from common import activate_language
from .services import PDFCreationService
from .models import Measurement, RightHand, LeftHand


class RightHandInlineAdmin(admin.StackedInline):
    model = RightHand


class LeftHandInlineAdmin(admin.StackedInline):
    model = LeftHand


@admin.register(Measurement)
class MeasurementAdmin(TranslationAdmin):
    list_display = (
        'id',
        'day_',
        'time_',
        'right_hand_',
        'left_hand_',
        'temperature_',
        'health',
        'is_bout_',
        'description_',
    )
    list_display_links = (
        'day_',
    )
    actions = [
        'export_to_pdf',
    ]
    list_filter = (
        'is_bout',
        'health',
        (
            'day',
            DateRangeFilter,
        ),
    )
    inlines = (
        RightHandInlineAdmin,
        LeftHandInlineAdmin,
    )

    @admin.display(description='Day')
    def day_(self, measurement: Measurement) -> str:
        return measurement.day_string

    @admin.display(description='Local time')
    def time_(self, measurement: Measurement) -> str:
        return measurement.time_string

    @admin.display(description=f'T\N{DEGREE SIGN}C')
    def temperature_(self, measurement: Measurement) -> str:
        return measurement.temperature

    @admin.display(description='Bout', boolean=True)
    def is_bout_(self, measurement: Measurement) -> bool:
        return measurement.is_bout

    @admin.display(description='Right hand')
    def right_hand_(self, measurement: Measurement) -> str:
        hand = measurement.hand_data(measurement.right_hand) # noqa
        return f'{hand.blood_pressure}/{hand.pulse}'

    @admin.display(description='Left hand')
    def left_hand_(self, measurement: Measurement) -> str:
        hand = measurement.hand_data(measurement.left_hand) # noqa
        return f'{hand.blood_pressure}/{hand.pulse}'

    @admin.display(description='Description')
    def description_(self, measurement: Measurement) -> str:
        language = getattr(measurement.user, 'language', settings.LANGUAGE_CODE)

        with activate_language(language):
            return measurement.description

    def save_model(self, request, obj, form, change):
        if not getattr(obj, 'user', None):
            obj.user = request.user

        super().save_model(request, obj, form, change)

    @admin.action(description='Export to PDF')
    def export_to_pdf(self, request, queryset) -> HttpResponse:
        with activate_language(request.user.language):
            pdf = PDFCreationService.create_pdf(queryset)

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
