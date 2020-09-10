from django.urls import include, path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),

]
