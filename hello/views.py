from django.shortcuts import render
from django.http import HttpResponse
from .apps import add
from django.views.generic.base import TemplateView
# Create your views here.


def hello(request):
    return render(request, 'hello.html')

def home(request):
    return render(request, 'home.html')

def map(request):
    return render(request, 'map18.html')

class a(TemplateView):
    template_name = 'a.html'
