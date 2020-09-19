from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('nfupload', views.nfupload, name='nfupload'),
    path('create1', views.create1, name='create1'),
    path('create2', views.create2, name='create2'),
    path('nhupload', views.nhupload, name='nhupload'),
    
    ]
