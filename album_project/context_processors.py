# lifted wholesale from http://stackoverflow.com/a/1433970/9947

from django.conf import settings


def adsense(request):
   """
   Returns the Adsense parameters
   """
   if not settings.DEBUG:
      return {'google_adwords_client': settings.GOOGLE_ADWORDS_CLIENT }
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
