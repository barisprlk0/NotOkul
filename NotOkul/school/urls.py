from django.conf.urls import url,include
from .views import *
from django.urls import path

app_name = 'school'
urlpatterns = [

    path('create', create ,name = "create"),
    path('delete/<int:id>/', delete, name="delete"),
    path('update/<int:id>/', update, name="update"),
    path('testsihirbazi',sihirbaz,name = "sihirbaz")
]
