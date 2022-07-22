from django.contrib import admin
from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('GOAL/<int:num>',views.GOAL,name='GOAL'),
    path('sample/<int:num>',views.sample,name='sample'),
    path('edit/<int:num>',views.edit,name='edit'),
]
