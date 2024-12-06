from .views import *
from django.urls import path

app_name = 'home'
urlpatterns = [

    path('', index , name = "home"),
    path('contact/',contact , name = "contact")
]
