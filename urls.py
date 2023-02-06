from django.urls import path
from .views import *

urlpatterns=[

    path('index/',index),
    path('registration/',register),
    path('login/',login123),
    path('user_registration/',regis),
    path('verify/<auth_token>',verify),
    path('user_login/',login),
    path('profile/',nav),
    # path('show/',file)
]