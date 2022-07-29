from modeltranslation import translator

from .models import Measurement


@translator.register(Measurement)
class MeasurementTranslationOptions(
    translator.TranslationOptions,
):
    fields = (
        'description',
    )
