# lifted wholesale from http://stackoverflow.com/a/1433970/9947

from django.conf import settings


def adsense(request):
    """
    Returns the Adsense parameters
    """
    if not settings.DEBUG:
        return {'google_adsense_id': settings.GOOGLE_ADSENSE_ID}
    else:
        return {}


def analytics(request):
    """
    Returns analytics code.
    """
    if not settings.DEBUG:
        return {'google_analytics_key': settings.GOOGLE_ANALYTICS_KEY}
    else:
        return {}
