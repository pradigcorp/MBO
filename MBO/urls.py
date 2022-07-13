from django.contrib import admin
from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
]