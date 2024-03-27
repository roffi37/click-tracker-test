from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework.decorators import api_view

from tracker.models import Tracker
from tracker.repository import check_short_url_in_base, add_short_url_to_base


def thank_you_page(request, clicked_url):
    short_url = check_short_url_in_base(clicked_url)
    if not short_url:
        short_url = add_short_url_to_base(clicked_url)
    return HttpResponse("Thank you for using our click tracker" 
                        f"short version of your link: {short_url}")


@api_view(["GET"])
def track_click(request, clicked_url):
    ip_address = request.META.get("REMOTE_ADDR")
    browser = request.META.get("HTTP_USER_AGENT")
    clicked_at = timezone.now()

    Tracker.objects.create(
        ip_address=ip_address,
        browser=browser,
        clicked_at=clicked_at,
        url=clicked_url
    )

    if request.path[-7:] == "origin/":
        return redirect("https://" + clicked_url)

    return thank_you_page(request, clicked_url)
