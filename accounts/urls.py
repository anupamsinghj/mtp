from django.urls import include, path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [

    path('register', views.register, name='register'),


]
