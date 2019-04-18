import arcpy
from arcpy import env
env.workspace = "D:\GISProjects\Exercise09\Exercise09.gdb"
env.scratchWorkspace = "D:\GISProjects\Exercise09\scratch.gdb"
env.overwriteOutput = True

#slope = arcpy.sa.Slope('elevation')

#print("the slope tool has run")

#slope.save("slope")
#print("the tool has successfully saved the slope")


from arcpy.sa import *
slope = Slope('elevation',"Degree")
aspect = Aspect('elevation')


#remap & reclassify
mydiv = RemapRange((([0,15,1], [15,100,0])))
mydiv2 = RemapRange((([-1,135,0], [135,225,1],[225,361,0])))

goodslope = Reclassify(slope,'value', mydiv)
goodaspect = Reclassify(aspect,'value',mydiv2)

#goodslope.save('goodslope')
#goodaspect.save('goodaspect')

solar = goodslope * goodaspect
solar.save('solarasd')


mydiv3 = RemapRange((([0,40,1],[40,43,0],[43,100,1])))
forestraster = Reclassify('LandCoverUTM','value',mydiv3)

bestsites = solar * forestraster

bestsites.save("solar2")

env.workspace = env.scratchWorkspace
dumpem = arcpy.ListDatasets()
for d in dumpem:
    arcpy.Delete_management(d)
