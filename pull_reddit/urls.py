from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.home, name='pull_reddit-home'),
]