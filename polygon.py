#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calculates area and perimeter of any polygon.

@author: D. Djokic

No warranties, at all. Really - no! 
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon


def polar_to_cart (r, ang_deg):
    theta=np.pi/180.0*ang_deg
    xcoord = r*np.cos(theta)
    ycoord = r*np.sin(theta)
    return xcoord, ycoord
    
inpfilename = raw_input("Input Filename: ")
coords = np.loadtxt(inpfilename, dtype=float, comments="#", delimiter=',', converters=None, skiprows=1, usecols=(0,1), unpack=False, ndmin=0)
print ("1 - Cartesian Coordinates \n2-Polar Coordinates")
choice = input ("Make a choice - 1 or 2: ")
num_pnt = len(coords)
coord1 = []
coord2 = []

for i in range(0, num_pnt):
    pnt = coords[i]
    coord1.append(pnt[0])
    coord2.append(pnt[1])
#print (coord1)
#print (coord2)

a =[]
xcoord = []
ycoord = []
if choice == 2:  # for polar coords
    for i in range (0, num_pnt):
        a = polar_to_cart (coord1[i], coord2[i])
        xcoord.append(a[0])
        ycoord.append(a[1])      
else: 
    xcoord = coord1
    ycoord = coord2

determ = []
perim = []
for i in range (1, num_pnt):
    a = xcoord[i-1]
    deter = xcoord[i-1]*ycoord[i] - xcoord[i]*ycoord[i-1]
    determ.append(deter)
    dist = abs(((xcoord[i]-xcoord[i-1])**2 + (ycoord[i]-ycoord[i-1])**2)**0.5)
    perim.append(dist)
    
area = 0.5*sum(determ)
perimeter = sum(perim)

print ("Area [sq. units]: ", area)
print ("Perimeter [units]: ", perimeter)

points = []
for i in range (0, num_pnt):
    temp = [xcoord[i],ycoord[i]]
    points.append(temp)
    
polygon = plt.Polygon(points)
plt.gca().add_patch(polygon)
plt.axis('scaled')
plt.show()


       
