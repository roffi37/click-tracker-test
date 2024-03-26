from django.db import models


class Tracker(models.Model):
    ip_address = models.CharField(max_length=39)
    browser = models.CharField(max_length=50)
    clicked_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.ip_address}"


class URL(models.Model):
    url = models.URLField()
    short_url = models.URLField()

    def __str__(self):
        return f"{self.url}"
