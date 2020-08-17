from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('home1/',log_in,name='home1'),
    ]