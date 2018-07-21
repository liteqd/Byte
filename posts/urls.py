# from django.conf import urls
from django.urls import path
from . import views

urlpatterns = [
    # url('', views.index, name="index")
    path('', views.index, name='index'),
]