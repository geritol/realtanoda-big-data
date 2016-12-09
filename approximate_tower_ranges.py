'''
source: http://gis.stackexchange.com/questions/6412/generate-points-that-lie-inside-polygon
'''

import random
import pylab as plt
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point

def get_random_point_in_polygon(poly):
     (minx, miny, maxx, maxy) = poly.bounds
     while True:
         p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
         if poly.contains(p):
             return p

orszag = Polygon([(17.1855, 47.9883), (16.5222, 47.7057), (16.5081, 47.3867), (16.2399, 46.9128), 
                   (17.4254, 45.9375), (18.4839, 45.8555), (19.5141, 46.1836), (20.6008, 46.1470), 
                    (21.1935, 46.4115),(22.3649, 47.7878), (22.7036, 47.8607), (22.8165, 48.0794), 
                    (22.2379, 48.3802), (21.25, 48.5078), (19.9234, 48.2526), (19.5423, 48.1523),
                    (18.7661, 47.8698), (17.8629, 47.724)])
                    


def gen(num):
    
    xs = []
    ys = []
    
    for i in range(num):
        point = get_random_point_in_polygon(orszag)
        xs.append(point.x)
        ys.append(point.y)
        
    plt.plot(xs, ys, '.')