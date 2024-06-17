from django.conf.urls import url,include
from .views import *
from django.urls import path

app_name = 'podcast'
urlpatterns = [
    path('create', create , name="create" ),




]
