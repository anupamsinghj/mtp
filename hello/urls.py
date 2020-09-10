from django.urls import include, path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.hello, name='hello'),
    #path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('a', TemplateView.as_view(template_name="a.html")),

    #path('add', views.add, name='add')

]
