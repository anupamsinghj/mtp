from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('nfupload', views.nfupload, name='nfupload'),
    path('create1', views.create1, name='create1'),
    path('create2', views.create2, name='create2'),
    path('create3', views.create3, name='create3'),
    path('info1', views.info1, name='info1'),
    path('info2', views.info2, name='info2'),
    path('nhupload', views.nhupload, name='nhupload'),

    ]
