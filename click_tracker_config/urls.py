from django.contrib import admin
from django.urls import path

from tracker import views


urlpatterns = [
    path("track/<clicked_url>/", views.track_click, name="track_click"),
    path("track/<clicked_url>/origin/", views.track_click, name="track_click_origin"),
    path("thank-you/", views.thank_you_page, name="thank_you_page"),
    path('admin/', admin.site.urls),
]
