from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('create_url/', views.CreateShortenedUrlView.as_view(), name='create_url'),
]
