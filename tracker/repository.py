from tracker.models import URL
from tracker.service import shorter_url_api


def check_short_url_in_base(url):
    try:
        short_url = URL.objects.get(url=url).short_url
        return short_url
    except URL.DoesNotExist:
        return False


def add_short_url_to_base(url):
    short_url = shorter_url_api(url)
    URL.objects.create(
        url=url,
        short_url=short_url
    )
    return short_url
