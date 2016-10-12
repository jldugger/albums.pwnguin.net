# lifted wholesale from http://stackoverflow.com/a/1433970/9947

from django.conf import settings
from django.template.loader import render_to_string


def analytics(request):
    """
    Returns analytics code.
    """
    if not settings.DEBUG:
        return {'google_analytics_key': settings.GOOGLE_ANALYTICS_KEY}
    else:
        return {}
