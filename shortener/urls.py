from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('create_url/', views.CreateShortenedUrlView.as_view(), name='create_url'),
    path('shorted_urls/', views.UrlListView.as_view(), name='url_list'),
    path('shorted_url/<pk>', views.UrlDetailView.as_view(), name='url_detail'),
]
