import arcpy
from arcpy import env

env.workspace = 'D:/GISProjects/Exercise05/Exercise05.gdb'

lyer = ['zip', 'hospitals','bike_routes','parks','facilities']
results = []
for i in lyer:
    deltx = arcpy.Describe(i).Extent.lowerLeft.X - arcpy.Describe(i).Extent.upperRight.X
    
    name = arcpy.Describe(i).name
    
    delty = arcpy.Describe(i).Extent.lowerLeft.Y - arcpy.Describe(i).Extent.upperRight.Y
    temparea = (abs(deltx*delty))
    sqmilearea = (temparea/5280 **2)
    results.append([sqmilearea,name])
results.sort()
for i in results:
    print('{0:15s} contains {1:7.2f} square miles'.format(i[1],i[0]))
# zip             contains    9.36 square miles
# hospitals       contains  285.39 square miles
# bike_routes     contains  497.08 square miles
# parks           contains  539.31 square miles
# facilities      contains 1178.35 square miles