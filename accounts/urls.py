from django.urls import include, path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('upload', views.upload, name='upload'),
    path('fupload', views.fupload, name='fupload'),
    path('hupload', views.hupload, name='hupload'),
    path('books', views.books, name='books'),
    path('books/uploadb', views.uploadb, name='uploadb'),
    path('create', views.create, name='create'),
]
