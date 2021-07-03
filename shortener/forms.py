from django import forms

from .models import ShortenedUrl


class CreateShortenedUrlForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ('original_url',)


