# Name: Hudson Chase
# Date: 03/04/2019
# Homework 4 
# 'Algorithms in GIS' - Great Circle Distance Calculation

import csv, numpy as np, math, pandas as pd
from numpy import array, zeros
from pprint import pprint
#from scipy.spatial import distance

infile = open('D:/VSProjects/Gainesville.csv','r')

import csv
li = []
for fields in csv.reader(infile, delimiter = ','):
    li.append(fields)

#print(li)
test = [item[4] for item in li]
test2 = [item[-2:] for item in li]
coords1 = (test[1:])
coords = np.array(test2[1:],float) #(test[1:])
name = test[1:]
#print (name)
#type(name)
#testcoords = (coords)
#print (coords)

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in miles
    return c * r

def calculateDistance(x1,y1,x2,y2):  
     x1 = x1
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
#def cart(y1, x1, y2, x2):
#    testx1 = R * math.cos(y1) * math.cos(x1)

#    testy1 = R * math.cos(y1) * math.sin(x1)

#    testx2 = R * math.cos(y1) * math.cos(x1)

#    testy2 = R * math.cos(y1) * math.sin(x1)

#    dist = math.hypot(testx2 - testx1, testy2 - testy1)
#    z = R * math.sin(y1)
#    return dist

N = coords.shape[0]
distance_matrix = zeros((N, N))
distance_matrix2 = zeros((N, N))
for i in range(N):
    for j in range(N):
        loni, lati = coords[i]
        lonj, latj = coords[j]
        distance_matrix[i, j] = haversine(loni, lati, lonj, latj)
        distance_matrix[j, i] = distance_matrix[i, j]
for i in range(N):
    for j in range(N):
        loni, lati = coords[i]
        lonj, latj = coords[j]
        #a = distance.cdist(coords, coords, 'cityblock')
        distance_matrix2[i, j] = calculateDistance(loni, lati, lonj, latj)
        distance_matrix2[j, i] = distance_matrix2[i, j]

df = pd.DataFrame(distance_matrix, index = (name), columns = (name) )
df2 = pd.DataFrame(distance_matrix2, index = (name), columns = (name) )
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)
np.triu(df)
print("The Great Circle Distance between these identically named points are as follows: (Distances are in Miles.) \n", df)
print("The Cartesian Distance between these identically named points are as follows: \n", df2)


