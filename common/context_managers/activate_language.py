import contextlib

from django.utils import translation


@contextlib.contextmanager
def activate_language(language):
    translation.activate(language)
    yield
    translation.deactivate()
