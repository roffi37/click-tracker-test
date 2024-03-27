from django.db import models


class Tracker(models.Model):
    ip_address = models.CharField(max_length=39)
    browser = models.CharField(max_length=50)
    clicked_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.ip_address} on {self.browser[:10]} at {str(self.clicked_at)[:16]} to {self.url}"


class URL(models.Model):
    url = models.URLField()
    short_url = models.URLField()

    def __str__(self):
        return f"Origin: {self.url} | Short: {self.short_url}"
