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
from .apps import draw_circle,map_base1,h_area, map_base, import_data, f_poly, i_poly, draw_map
####################################################
def info1(request):
    return render(request, 'info.html')

def info2(request):
    return render(request, 'info2.html')

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
            #messages.info(request,'file succesfully uploaded ')
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


def nhupload(request): # to get file and buffer radius for hotspot regoin
    context={}
    global pointss, gmapp, fnn ,bf
    if request.method == 'POST':
        bf = float(request.POST["bf"])
        uploaded_file = request.FILES['hfile']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        fnn = uploaded_file.name
        print(uploaded_file)
        if 'csv' in uploaded_file.name:
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
            print('anu' + str(fs.url(name))[1:])
            #messages.info(request,'file succesfully uploaded ')
            pointss,cor = import_data(str(fs.url(name))[1:])
            #gmap=map_base(points,zoom=12)
            abc=fnn
            return render(request, 'hnhupload.html',{'hfn':abc, 'fn':fn, 'bf':bf}  )
        else :
            messages.info(request,'ERROR : upload only csv file ')
            return redirect('nhupload')
    else :
        return render(request, 'hnhupload.html')

def create1(request):  # to get lat, long and radius for a 2nd option
    #file_name='media/' + abc
    global lat, lon, radius, buffer_radius
    if request.method == 'POST':
                lat = float(request.POST['lat'])
                lon = float(request.POST['lon'])
                radius = float(request.POST['radius'])
                buffer_radius = float(request.POST['bradius'])

                return render(request, 'nnhupload.html',{'fn': fn,'lat': lat,'lon': lon, 'radius': radius, 'buffer_radius': buffer_radius})

def create2(request):   # for the 2nd options for entering hotspot region
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
def create3(request):
    bff= bf
    if request.method == 'POST':
                        #print(lat + lon, radius)
                        area = h_area(pointss)
                        zz= i_poly(area,points)
                        #bf= bf
                        b_area,z,b_line=f_poly( area,points,bff)
                        gmap=map_base(pointss,zoom=12)
                        draw_map(gmap,z,area,b_area,b_line,cor)
                        print('run succesfully')
                        return render(request, 'hhnhupload.html',{'hfn':fnn, 'fn':fn, 'bf':bf})
