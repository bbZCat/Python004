from django.urls import path
from . import views

urlpatterns = [
    path('login', views.userlogin),
    path('index', views.index),
    path('', views.userlogin),
]
