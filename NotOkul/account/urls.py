from .views import *
from django.urls import path


app_name = "account"

urlpatterns = [
    path('register/' , register_view , name = "register"),
    path('login/' , login_view , name = "login"),
    path('logout/' , logout_view , name = "logout"),
    path('profile/', profile , name='profile'
),
    ]
