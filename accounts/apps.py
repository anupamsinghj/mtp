from django.apps import AppConfig
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shapely
import json
import geog
import shapely.geometry
from shapely.ops import polygonize,unary_union
from scipy.spatial import Voronoi,voronoi_plot_2d
from geovoronoi import voronoi_regions_from_coords
from shapely.geometry import MultiLineString, MultiPolygon,LinearRing,MultiPoint,Point,LineString,Polygon
from descartes import PolygonPatch
import gmplot
from gmplot import *


class AccountsConfig(AppConfig):
    name = 'accounts'

def draw_circle(array=[],lat=0,lon=0,radius=0):
    if len(array)==0:
        x= Point(lat,lon).buffer(radius/110.5)
    else :
        a=1
    return Polygon(x)

def map_base(lat=28.0760,lon= 77.8777,zoom=12):
    gmap=gmplot.GoogleMapPlotter(lat,lon,zoom)
    gmap.apikey = "AIzaSyCeM999Sqh_Vfo4ZZMAmMUJyRQcl78SyRw"
    gmap.draw( "templates/abc.html" )
    #gmap.circle(19.076956, 72.848481, 8000,'red')
    print('map_created')
    return gmap

def import_data(file_name):
    df=pd.read_csv(file_name)
    df=df.drop_duplicates(subset=['lon','lat'])
    lat=df['lat']
    lon=df['lon']
    points = np.stack((lat,lon), axis=1)
    cor={'lat':lat,'lon':lon}

    return points,cor

def i_poly(area,points):

    x=area
    vor = Voronoi(points)
    #print(vor)
    lines = [
    shapely.geometry.LineString(vor.vertices[line])
    for line in vor.ridge_vertices
    if -1 not in line]


    z=[]
    for poly in polygonize(lines) :
        if area.intersects(poly):
            z.append(poly)

    return MultiPolygon(z)

def f_poly( area,points,buffer_radius):
    x=area
    vor = Voronoi(points)
    lines = [shapely.geometry.LineString(vor.vertices[line]) for line in vor.ridge_vertices if -1 not in line]

    xx = x.convex_hull.buffer(buffer_radius/110)
    result = MultiPolygon(
    [poly.intersection(xx) for poly in polygonize(lines)])

    z=[]
    for poly in result :
        if x.intersects(poly):
            z.append(poly)

    #print(z)
    b_area=MultiPolygon(z)
    b_line=xx
    return b_area,z,b_line

def draw_map(gmap,z,area,b_area,b_line,cor):
    bc=b_area
    xx=b_line
    x=area
    bc=MultiPolygon(z)
    xs, ys = x.exterior.xy
    xss,yss= xx.exterior.xy
    zx=shapely.ops.unary_union(bc)
    xsss,ysss= zx.exterior.xy
    lat=cor['lat']
    lon=cor['lon']
    gmap.scatter( lat, lon, 'b', size = 40, marker = True )
    gmap.plot(xsss,ysss,
             'r', edge_width = 2.5)
    gmap.plot(xss,yss,
             'black', edge_width = 2.5)
    gmap.plot(xs,ys,
             'y', edge_width = 2.5)

    for abc in z:
        xt, yt = abc.exterior.xy
        gmap.polygon(xt, yt,
                       color = 'orange')
    gmap.draw("templates/abc.html")
    print("C:\\Users\91963\\project1\\templates\\map19.html")

    return None
