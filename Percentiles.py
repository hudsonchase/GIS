#import the needed libraries (arcpy, os, numpy)
#get the environment
import arcpy, os, numpy
from arcpy import env

#set the workspace to c:/GISProjects/exercise09a
env.workspace = 'D:/GISProjects/exercise09a'
path = env.workspace 
env.overwriteOutput = True

#request the raster to analysze from the user
inraster = input("Which raster do you want to analyze? ")
#get the raster projection units for area calculation
inunits = arcpy.Describe(inraster)
uname = inunits.spatialReference.linearunitname
#set the output paths to write a file called temp.flt 
#(tmp.hdr is automatic, but we need to read it)
outfile = path + '/tmp.hdr'
outfile2 = path + '/tmp.flt'
#run the raster to float conversion
arcpy.RasterToFloat_conversion(inraster,outfile2)
#open the header of the raster to read as ASCII
infile = open(outfile,'r')
#read the header file and split for important values
datain = infile.read()
temp = datain.split()
#get the number of columns - first line
ncols = int(temp[1])
#get the number of rows - second line
nrows = int(temp[3])
#get the cellsize (for area computation) - fifth line
cellsize = float(temp[9])
#get the NoData value for removing NoData cells - sixth line
nodata = float(temp[11])

#report on the above raster properties to the user
arcpy.AddMessage("\n\nRaster properties\n")
arcpy.AddMessage("Columns:      " + str(ncols))
arcpy.AddMessage("Rows:         " + str(nrows))
arcpy.AddMessage("cellsize:     " + str(cellsize))
arcpy.AddMessage("NoData Value: " + str(nodata))
arcpy.AddMessage("Area Unit:    " + str(uname))


#compute and report the total cells
numvals = nrows*ncols
arcpy.AddMessage("Total cells:  " + str(numvals))

#numpy fromfile will read the data into a new numpy array, then sort the array
values = numpy.fromfile(outfile2,'f')
values.sort()

#IMPORTANT FOR HOMEWORK 7 BOOLEAN ARRAY -- check all values for NoData with numpy where - returns indices that are True
values2 = numpy.where(values != nodata)

#create new array for only the true values by the boolean array values2
values3 = values[values2]

#report the removal of NoData values from the list
arcpy.AddMessage('removed {0:7d} missing data values from the raster leaving {1:7d} '\
   'values to process'. format(len(values)-len(values3), len(values3)))
print('')
#close and delete (remove) the temporary files to save memory
del values
del values2
infile.close()
os.remove(outfile)
os.remove(outfile2)

#report on the percentiles and areas in a table
#write a header title
arcpy.AddMessage('\n\nPercentiles of ' + inraster + ' and cummulative area in square miles\n')
arcpy.AddMessage('Percentile       Value       area below       area above')
arcpy.AddMessage('--------------------------------------------------------\n')

#compute the number of values in a percent of the total array - make an integer
nonmissing = len(values3)
onepct = nonmissing // 100

#compute the total area of the raster cells with data in native units
area = nonmissing*(cellsize**2)

#set conversions from the native units to square miles: 
if uname == "Meter":
    convert = float(1609**2)
elif uname == "Mile":
    convert = float(1**2)
elif uname == "Foot":
    convert = float(5280**2)
else:
    convert = 1.0
#meters converts by 1609*1609
#mile converts by 1.0
#foot converts by 5280*5280
#also allow for unknown to convert by 1.0

#convert total area to square miles
totarea = area/convert

#initialize a counter to 1 and print the minumum value line
pct = 1
arcpy.AddMessage('{0:^10s}  {1:10.2f}   {2:15.2f}   {3:15.2f}'. \
    format('Minimum', float(values3[0]), 0.0, totarea))

#iterate the array, by 1% and print out the current values for the table
for i in range(onepct,nonmissing-onepct, onepct):
    arealess = i*cellsize**2/convert
    areamore = totarea-arealess
    arcpy.AddMessage('{0:^10d}  {1:10.2f}   {2:15.2f}   {3:15.2f}'. \
        format(pct, float(values3[i]), arealess, areamore))
    pct+=1
#print the maximum
arcpy.AddMessage('{0:^10s}  {1:10.2f}   {2:15.2f}   {3:15.2f}'. \
    format('Maximum', float(values3[-1]), totarea, 0.0))

        
