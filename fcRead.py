import arcpy
from arcpy import env
env.workspace = "D:/GISProjects/exercise08/exercise08.gdb"
fc = "Hawaii"

# get a searchcursor on the feature class
# to collect the OID and the shape object
cursor = arcpy.da.SearchCursor(fc, ['OID@', 'SHAPE@'])

# triple nest iterates to read all points in all parts - so little code - iterations are GREAT!!!
# Objects are great too - is this easier than reading the shapefile in binary?
for row in cursor:
    print("Feature {0:3d}: ".format(row[0]))
    partnum = 0

    #then parts
    for part in row[1]:
        print ("Part {0:3d}: ".format(partnum))
        lix = []
        liy = []

        #then points
        for point in part:
            lix.append(point.X)
            liy.append(point.Y)
           #print ("{0:8.0f}, {1:8.0f}".format(point.X, point.Y))

        print("Mean Center for part is: {0:10.2f}, {1:10.2f}".format(sum(lix)/len(lix), sum(liy)/len(liy)))
        partnum += 1
