from django.urls import path
# from django.conf import urls

from . import views

urlpatterns = [
    path('', views.homePageView, name='homePageView'),
]