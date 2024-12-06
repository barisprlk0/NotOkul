from django.urls import re_path
from .views import *

app_name = 'school'
urlpatterns = [
    re_path(r'^create$', create, name="create"),
    re_path(r'^delete/(?P<id>\d+)/$', delete, name="delete"),
    re_path(r'^update/(?P<id>\d+)/$', update, name="update"),
    re_path(r'^testsihirbazi$', sihirbaz, name="sihirbaz"),
]
