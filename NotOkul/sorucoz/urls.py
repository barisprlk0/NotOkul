from .views import *
from django.urls import path
from sorucoz.views import ClupChartView
app_name = 'sorucoz'
urlpatterns = [
    path('', ClupChartView.as_view(),name="index")
]
