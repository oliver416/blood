import io
from collections import defaultdict

import pdfkit

from django.db.models.query import QuerySet
from django.template import loader


class PDFCreationService:
    TEMPLATE = 'diary/health_diary.html'
    PDF_NAME = 'health_diary.pdf'

    @classmethod
    def create_pdf(cls, queryset: QuerySet) -> bytes:
        table_data = cls._prepare_table_data(queryset)
        html = loader.render_to_string(cls.TEMPLATE, context={'context': table_data})
        pdf = io.BytesIO(
            pdfkit.PDFKit(html, 'string').to_pdf(),
        )
        return pdf.read()

    @classmethod
    def _prepare_table_data(
        cls,
        queryset: QuerySet,
    ) -> dict:
        table_data = defaultdict(list)

        for measurement in queryset.order_by('day', 'time'):
            left_hand = measurement.hand_data(
                getattr(measurement, 'left_hand', None),
            )
            right_hand = measurement.hand_data(
                getattr(measurement, 'right_hand', None),
            )
            temperature = measurement.temperature or '-'
            description = measurement.description or '-'

            measurement_data = {
                'time': measurement.time_string,
                'temperature': temperature,
                'description': description,
                'left_hand_blood_pressure': getattr(left_hand, 'blood_pressure', '-'),
                'right_hand_blood_pressure': getattr(right_hand, 'blood_pressure', '-'),
                'left_hand_pulse': getattr(left_hand, 'pulse', '-'),
                'right_hand_pulse': getattr(right_hand, 'pulse', '-'),
            }
            table_data[measurement.day_string].append(measurement_data)

        return dict(table_data)

