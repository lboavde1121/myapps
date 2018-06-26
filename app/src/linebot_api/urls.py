from django.urls import path

from . import views

urlpatterns = [
    path('tweet', views.Tweet.as_view(), name='tweet'),
    path('save_oauth_token', views.save_oauth_token, name='save_oauth_token'),
]
