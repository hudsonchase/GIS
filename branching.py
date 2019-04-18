import arcpy

# Choose one of many options depending on the input feature type
#get the feature layer from the model
InputFile = arcpy.GetParameterAsText(0)    #first parameter from the model or script design
#InputFile = "D:/GISClass/Conditional/Conditional.gdb/City_Limit"
#Create a Describe Object that will offer the feature type
DescFile = arcpy.Describe(InputFile)        #Stores the type in the property shapeType

#Check the Shapetype and respond appropriately
if DescFile.shapeType == "Point":
    arcpy.AddMessage ("These are point features.")
    
        
elif DescFile.shapeType == "Polyline":
    print ("It's a polyline")
    arcpy.AddMessage ("\n\nThese are line features.\n\n")

    
elif DescFile.shapeType == "Polygon":
    arcpy.AddMessage ("These are polygon features.")

else:
    arcpy.AddMessage("This is not type I can deal with here.")

arcpy.MakeFeatureLayer_management(InputFile, 'temp')
arcpy.conversion.LayerToKML('temp',"D:/GISProjects/conditional/kmzout.kmz")

    
                  
                      

