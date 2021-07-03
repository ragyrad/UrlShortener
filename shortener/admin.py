from django.contrib import admin

from .models import ShortenedUrl


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ('shortened_url', 'created')
    search_fields = ('shortened_url',)
    ordering = ('created',)