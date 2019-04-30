import census
from census import Census
from us import states
import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = 'D:/GISProjects/census/census.gdb'

#fileout = input('Enter the name of the new table in the GeoDatabase: ')
#fileout = "test"
fileout = arcpy.GetParameterAsText(0)

newtab = arcpy.CreateTable_management(env.workspace,fileout)

#tuple of fields to be downloaded
fields = ('NAME', 'STATE', 'COUNTY','TRACT', 'B25077_001E')#P012001', 'P012002', 'P012026')

#add geography fields as text fields
for i in range(0,4):
    arcpy.AddField_management(newtab, fields[i],"TEXT")

#continue table build - add data fields as doubles
for i in range(4,len(fields)):
    arcpy.AddField_management(newtab,fields[i], "Double")

#add a new key field for TIGER
arcpy.AddField_management(newtab,"TigerKey", "TEXT")

#insert cursor to all fields to add the data to fields
cursor = arcpy.da.InsertCursor(newtab,"*")

#hardcode state and county fips code for data download
state = '51'
county = '121'

#Get data from Census API
c = Census('bf305bc6372c5f202b992a9b4f450931e26b0628', 2017)

#request and collect data
recs = c.acs5.state_county_tract(fields,state,county,Census.ALL)
num = len(recs)

# process table row by row
for i in range (0,num):
    #build the TigerKey field
    TigerKey = recs[i]['STATE'] + recs[i]['COUNTY'] + recs[i]['TRACT']
    #build the field values list/tuple
    row = []
    row.append(i)
    for j in range(0, len(fields)):
        row.append(recs[i][fields[j]])
    #add the key computed above
    row.append(TigerKey)
    #insert the new row
    cursor.insertRow(row)

del cursor

arcpy.AddMessage("\nTable   {0:s} created. \n {1:4d} rows written with text field \n 'TIGERKey' added for joins to TIGER tract data."\
    .format(newtab[0], num))

