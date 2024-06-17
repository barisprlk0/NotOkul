from django.conf.urls import url,include
from .views import *
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('index', index , name='index'),
    path('delete/<int:id>', delete , name='delete'),
    path('complete/<int:id>' , complete , name='complete' ),
    path('update/<int:id>' , update , name='update' ),

]
