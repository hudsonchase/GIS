import arcpy, os, zipfile
import wget
from arcpy import env
env.workspace='D:/gisprojects/Prism/prism.gdb'   

#url = "http://services.nacse.org/prism/data/public/4km/"
#element = "ppt"
#dt = '/20090405'
#url = url + element + dt 
#wget.download(url, 'D:/GISProjects/Prism/20090405.zip')

#Output directory for data downloaded - enter path to the arc workspace
filedir = "D:/GISProjects/Prism"

#change to output directory with os.chdir(....


#date for which data will be downloaded 
#datestr = input("Enter the date for the data you want as mm/dd/yyyy: ")
datestr = arcpy.GetParameterAsText(0)

#request variable desired
#var = input("Enter the variable you want (ppt, tmin,tmax): ")
var = arcpy.GetParameterAsText(1)

#get the output raster layer name
nrl = arcpy.GetParameterAsText(2)
#nrl = 'test'

arcpy.AddMessage("\n\nGetting "+ var + " data for " + datestr + "\n\n")

#separate the date into smonth, sday, and syear and assign to variables
smonth = datestr.split('/')[0]
sday = datestr.split('/')[1]
syear = datestr.split('/')[2]
if len(smonth) < 2:
   smonth = smonth.rjust(2, '0')
if len(sday) < 2:
   sday = sday.rjust(2, '0')
#set the prism file code for var (prism files use a differnt code in the filename by types
if var == 'ppt':
    dval = 'D2'
else:
    dval = 'D1'

#create a new folder with the year in output folder
#set the name
yeardir = filedir + '\\' + syear


#if it does not already exist, make a new one
if os.path.exists(yeardir) == False:
    os.mkdir(yeardir)
    print("Created a new folder")
else:
    print("Folder already exists")

#change to the directory whether just created or not
os.chdir(yeardir)

#create a new directory inside the year directory (if needed) for the variable to be downloaded
#set the name
outdir = yeardir + '\\' + var

#if it does not already exist, make a new one
if not os.path.exists(outdir):
    os.mkdir(outdir)

#change to the directory whether just created or not
os.chdir(outdir)
     
#make a string (day) to match the format of the download file for the day to retrieve 
#based on the dcumentation from prism (year, 2 character month, 2 character day)
day = syear+smonth+sday 

#create the rest of the prism file name format (http location + variable + the day to retrieve as getfile
getfile = 'http://services.nacse.org/prism/data/public/4km' + '/' +  var + '/' + day

#check if the file has been downloaded previously and skip if so (use variable 'name')
name = outdir + '\\' + day
if os.path.exists(name):
 arcpy.AddMessage("File " + name + " already exists.  Download is skipped")

#notify that the file will be downloaded
else:
    arcpy.AddMessage("\n\nRetrieving " + getfile)
    
    #use wget to download the file with os.system
    prismfile = wget.download(getfile, name)
    #unzip the zip files
    zfile = zipfile.ZipFile(name)
    zfile.extractall()

#make the possible bil file names - 3 are possible - check for which one exists (stable, provisional, or early)
bilfile1 = 'PRISM_' + var + '_early_4km' + dval + '_'+ day +"_bil" + ".bil"
bilfile2 = 'PRISM_' + var + '_provisional_4km' + dval + '_'+ day +"_bil" + ".bil" 
bilfile3 = 'PRISM_' + var + '_stable_4km' + dval + '_'+ day +"_bil" + ".bil" 



if os.path.exists(bilfile1):
    bilfile = bilfile1
elif os.path.exists(bilfile2):
    bilfile = bilfile2
else:
    bilfile = bilfile3

bilpath = outdir + "\\" + bilfile

#report that you are loading the map into the current map view (when we get this into arcGIS) - does not work in external
#script tests - but you can manually add the layer to see that it was downloaded correctly.
arcpy.SetParameterAsText(2, bilpath)

