import arcpy
import arcpy.da
import os
from arcpy import env
env.workspace = "D:/GISProjects/exercise08/exercise08.gdb"
env.overwriteOutput = True
outpath = env.workspace
newfc = "fishingtrip"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
infile = "D:/GISprojects/exercise08/coordinates.txt"

#get a cursor on the new feature class geometry object
cursor = arcpy.da.InsertCursor(newfc,["SHAPE@"])
#create a new arcpy array object with no assigned type (yet)
array = arcpy.Array()

#read the points from the file into point objects (then add then to the array)
filein = open(infile, 'r')
for line in filein:
    ID, X, Y = line.split()
    array.add(arcpy.Point(X,Y))
cursor.insertRow([arcpy.Polyline(array)])
filein.close
del cursor

desc = arcpy.Describe("Hawaii")
coordsys = desc.spatialReference
arcpy.DefineProjection_management(newfc,coordsys)

#set the projection to match the existing Hawaii layer
