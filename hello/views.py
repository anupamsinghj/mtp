from django.http import HttpResponse
from django import forms
from .apps import add
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
# Create your views here.


def hello(request):
    return render(request, 'hello.html')

def home(request):
    return render(request, 'home.html')

def map(request):
    return render(request, 'map18.html')
'''
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/')
    else :
        return render(request, 'register.html')'''

class a(TemplateView):
    template_name = 'a.html'
