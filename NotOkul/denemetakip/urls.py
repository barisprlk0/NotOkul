from django.urls import path
from .views import *

app_name = "denemetakip"

urlpatterns = [
    path('create', create, name='create'),
    path('index', index, name='index'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
    #ayt
    path('createAYT', createAYT, name="createAYT"),
    path('deleteAYT/<int:id>', deleteAYT, name='deleteAYT'),
    path('updateAYT/<int:id>', updateAYT, name='updateAYT'),

]
