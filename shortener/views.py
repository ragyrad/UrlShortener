import random
import string

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import CreateShortenedUrlForm
from .models import ShortenedUrl
from config.settings import DOMAIN


class MainPageView(View):

    def get(self, request):
        return render(request, 'shortener/main.html')


def generate_shortened_url():
    return DOMAIN + '/' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class CreateShortenedUrlView(View):

    def get(self, request):
        form = CreateShortenedUrlForm()
        return render(request, 'shortener/create_url.html', {'form': form})

    def post(self, request):
        form = CreateShortenedUrlForm(request.POST)
        shortened_url = None
        if form.is_valid():
            existed_urls = [url.shortened_url for url in ShortenedUrl.objects.all()]
            while True:
                shortened_url = generate_shortened_url()
                if shortened_url not in existed_urls:
                    break
            new_url = form.save(commit=False)
            new_url.shortened_url = shortened_url
            new_url.original_url = form.cleaned_data['original_url']
            new_url.save()

        return render(request, 'shortener/create_url.html', {'form': form,
                                                             'shortened_url': shortened_url})


class UrlListView(ListView):
    model = ShortenedUrl
    context_object_name = 'url_list'


class UrlDetailView(DetailView):
    model = ShortenedUrl
    context_object_name = 'url'
