from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage#, OverwriteStorage
from .models import Book, OverwriteStorage, uploadf
####################################################
                # IMPORTING FUNCTION FROM APP
from .apps import draw_circle,map_base1, map_base, import_data, f_poly, i_poly, draw_map
####################################################


def nupload(request):
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



def n1fupload(request):
    if 'csv' in uploaded_file.name:
        i=1
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        i+=1
        messages.info(request,'file succesfully uploaded ')
        points,cor = import_data('media/' + fn)
        gmap=map_base(points,zoom=12)
        abc=fn
        return render(request, 'nhupload.html',{'abc':abc}  )



def nfupload(request):
    context={}
    global fn
    global uploaded_file
    global points
    global cor, gmap
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        fn = uploaded_file.name
        #print(fn)
        print(uploaded_file)
        if 'csv' in uploaded_file.name:
            i=1
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
            print('anu' + str(fs.url(name))[1:])
            messages.info(request,'file succesfully uploaded ')
            points,cor = import_data(str(fs.url(name))[1:])
            gmap=map_base(points,zoom=12)
            abc=fn
            return render(request, 'nhupload.html',{'abc':abc}  )


        else :
            messages.info(request,'ERROR : upload only csv file ')
            return redirect('nfupload')

        #return redirect('/')
    else :
        return render(request, 'nfupload.html',context)


def nhupload(request):
    context={}
    abc = fn
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
            return redirect('nhupload')

        #return redirect('/')
    else :
        return render(request, 'nhupload.html',{'fn': abc})


def create1(request):
    #file_name='media/' + abc
    global lat, lon, radius, buffer_radius
    if request.method == 'POST':
                lat = float(request.POST['lat'])
                lon = float(request.POST['lon'])
                radius = float(request.POST['radius'])
                buffer_radius = float(request.POST['bradius'])

                return render(request, 'nnhupload.html',{'fn': fn,'lat': lat,'lon': lon, 'radius': radius, 'buffer_radius': buffer_radius})

def create2(request):
    if request.method == 'POST':
                        print(lat + lon, radius)
                        area = draw_circle(lat=lat,lon = lon,radius= radius )
                        zz= i_poly(area,points)
                        bf=buffer_radius -  radius
                        b_area,z,b_line=f_poly( area,points,bf)
                        gmap=map_base1(lat=lat,lon= lon,zoom=12)
                        draw_map(gmap,z,area,b_area,b_line,cor)
                        print('run succesfully')
                        return render(request, 'nnnhupload.html',{'fn': fn,'lat': lat,'lon': lon, 'radius': radius, 'buffer_radius': buffer_radius})
