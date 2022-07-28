import io

import pdfkit

from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.template import loader


class PDFCreationService:
    TEMPLATE = 'diary/health_diary.html'
    PDF_NAME = 'health_diary.pdf'

    @classmethod
    def create_pdf(cls, request: HttpRequest, queryset: QuerySet) -> bytes:
        html = loader.render_to_string(cls.TEMPLATE, context={})
        pdf = io.BytesIO(
            pdfkit.PDFKit(html, 'string').to_pdf(),
        )
        return pdf.read()
