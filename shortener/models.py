from django.db import models


class ShortenedUrl(models.Model):
    original_url = models.URLField(max_length=1000)
    shortened_url = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.shortened_url
