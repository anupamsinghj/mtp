# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:58:10 2020

@author: anupam
"""
## importing package
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shapely
from shapely.ops import polygonize,unary_union
from scipy.spatial import Voronoi,voronoi_plot_2d
from geovoronoi import voronoi_regions_from_coords
#from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from shapely.geometry import MultiLineString, MultiPolygon,LinearRing,MultiPoint,Point,LineString,Polygon
from descartes import PolygonPatch


import gmplot
from gmplot import *


def bc():
    a=input("enter file name:")
    df=pd.read_csv('a')
    df=df.drop_duplicates(subset=['lon','latt'])
    lat=df['latt']
    lon=df['lon']
    points = np.stack((lat,lon), axis=1)
    vor = Voronoi(points)

    lines = [
    shapely.geometry.LineString(vor.vertices[line])
    for line in vor.ridge_vertices
    if -1 not in line]

    ppp= shapely.ops.polygonize(lines)
    pppp=MultiPolygon(ppp)

    x  =Point(28.61,77.2250).buffer(0.005125)

    z=[]
    for poly in polygonize(lines) :
        if x.intersects(poly):
            z.append(poly)

    z=MultiPolygon(z)

    xx = x.convex_hull.buffer(0.15)
    result = MultiPolygon(
    [poly.intersection(xx) for poly in polygonize(lines)])

    z=[]
    for poly in result :
        if x.intersects(poly):
            z.append(poly)

    bc=MultiPolygon(z)
    xs, ys = x.exterior.xy
    xss,yss= xx.exterior.xy
    zx=shapely.ops.unary_union(z)
    xsss,ysss= zx.exterior.xy


    gmap2 = gmplot.GoogleMapPlotter(28.6760,
                                77.4777, 13 ,apikey="AIzaSyCeM999Sqh_Vfo4ZZMAmMUJyRQcl78SyRw")
    gmap2.scatter( lat, lon, 'b', size = 40, marker = True )
    gmap2.plot(xsss,ysss,
             'r', edge_width = 2.5)
    gmap2.plot(xss,yss,
             'black', edge_width = 2.5)
    gmap2.plot(xs,ys,
             'y', edge_width = 2.5)

    for abc in z:
        xt, yt = abc.exterior.xy
        gmap2.polygon(xt, yt,
                       color = 'orange')
    gmap2.draw( "C:\\Users\91963\\Desktop\\map14.html" )

    return None

