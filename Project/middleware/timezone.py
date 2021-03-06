import contextlib

from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = None # noqa

        with contextlib.suppress(AttributeError):
            tzname = request.user.timezone

        if tzname:
            timezone.activate(tzname)
        else:
            timezone.deactivate()

        return self.get_response(request)
