from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate
#from .apps import add
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .forms import BookForm
from .models import Book
####################################################
                # IMPORTING FUNCTION FROM APP
from .apps import draw_circle, map_base, import_data, f_poly, i_poly, draw_map
####################################################

def create(request):
    file_name='media/ffile.csv'
    buffer_radius=2
    points,cor = import_data(file_name)
    gmap=map_base(lat=28.5760,lon= 77.2777,zoom=12)
    if request.method == 'POST':
                lat = float(request.POST['lat'])
                lon = float(request.POST['lon'])
                radius = float(request.POST['radius'])
                print(lat + lon,radius)
                area=draw_circle(lat=lat,lon = lon,radius= radius )
                zz=i_poly(area,points)
                b_area,z,b_line=f_poly( area,points,buffer_radius)
                b_area,z,b_line=f_poly( area,points,buffer_radius)
                draw_map(gmap,z,area,b_area,b_line,cor)
                print('run succesfully')
                return redirect('hupload')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 ==  password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else :
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User created')

        else :
            messages.info(request,'password not matching' )
            return redirect('register')
        return redirect('/')
    else :
        return render(request, 'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,'You entered wrong credential' )
            return redirect('login')

    else :
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        print(uploaded_file)
        if 'csv' in uploaded_file.name:
            i=1
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
            i+=1
            return render(request, 'upload.html',context)
        else :
            messages.info(request,'you have not uploade a csv file')
            return redirect('upload')

        return redirect('/')
    else :
        return render(request, 'upload.html',context)

def fupload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        print(uploaded_file)
        if 'csv' in uploaded_file.name:
            i=1
            name = fs.save('ffile.csv', uploaded_file)
            context['url'] = fs.url(name)
            i+=1
            messages.info(request,'file succesfully uploaded ')
            return render(request, 'fupload.html',context)

        else :
            messages.info(request,'ERROR : upload only csv file ')
            return redirect('fupload')

        #return redirect('/')
    else :
        return render(request, 'fupload.html',context)


def hupload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['hfile']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        print(uploaded_file)
        if 'csv' in uploaded_file.name:
            i=1
            name = fs.save("hfile.csv", uploaded_file)
            context['url'] = fs.url(name)
            i+=1
            messages.info(request,'file succesfully uploaded ')
            return render(request, 'hupload.html', context)
        else :
            messages.info(request,'ERROR : upload only csv file ')
            return redirect('hupload')

        #return redirect('/')
    else :
        return render(request, 'hupload.html',context)



def books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

def uploadb(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })
