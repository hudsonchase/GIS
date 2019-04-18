# Name: Hudson Chase
# Date: 02/12/2019
# Homework 2
# 'Algorithms in GIS' - Read GEOJSON as strings

# geojsonfile= "D:\Downloads\MCTYRests.geojson"
# "D:\Downloads\cities2.json"

def geojsonstr(jsonfile):
    #open the GeoJSON file and read the whole thing into a string FIND FIELD NAME sequesces adn indexes
    filein = open(jsonfile,'r')
    stringin = filein.read()
    filein.close()
    begin = 0
    beginname = 0
    beginadd = 0
    i = 0
    
    coordinates = []
    name = []
    restnames = []
    addresses = []
    while i < len(stringin):
        startlong = stringin.find('coordinates":[-', begin, -1)
        startname = stringin.find('USER_Restaurant":"', beginname,-1) 
        startadd = stringin.find('USER_Address":"', beginadd,-1)
        #print (startlong)
        test2 = stringin[startname+17: -1]
        test3 = test2.split('",')
        #print(test3)
        test4 = stringin[startadd+15: -1]
        test5 = test4.split('"}')
        addresses.append(test5[0])
        readlong = stringin[startlong+14:startlong+52]
        test = readlong.split(",")
        
        #print (test2)
        restnames.append(test3[0])
        #print (restnames)
        coordinates.append(test)
        begin = startlong + 1
        beginname = startname + 1
        beginadd = startadd + 1
        #print (test)
        i = (len(stringin)-(startlong)) 
    
    del coordinates[-1]
    
    print ("The name of the restaurants are as follows:",restnames)
    print ("The addresses of the restaurants are:", addresses)
    print ("The coordinates are Longitude and Latitude shown accordingly:", coordinates)
    print ("\nSummary Statistics:")
    print ("There are", len(coordinates), "restaurants listed in this file")
    
   # stringcoordmath1 = stringcoordmath.split(",")
    latmax = max(coordinates, key=lambda x:x[1])
    print("\nThe max latitude is: ", latmax[1])

    latmin = min(coordinates, key=lambda x:x[1])
    print("The min latitude is: ", latmin[1])

    newcoordlist = []
    newcoordlist2 = []
    
    #latspre = [list(row) for row in coordinates]
    
    #print(latspre)
    #coordinates = map(coordinates.strip("]"), coordinates)
    for item in coordinates:
        newcoordlist.append(float(item[0]))
        #newcoordlist2.append(item[1])
    #print (newcoordlist2)
   
    #a = (lambda x:x[1:-1], coordinates)
       
    
    #sumlats = float(sum(x[1] for x in latspre))
    #print (sumlats)
    #meanlats = sumlats/len(latspre)
    #print(meanlats)
    #print(newcoordlist)
    print ("The mean of the longitudes are: " , sum(newcoordlist)//len(newcoordlist))
    def median(l):
        half = len(l) // 2
        l.sort()
        if not len(l) % 2:
            return (l[half - 1] + l[half]) / 2.0
        return l[half]
    print ("The median of the longitudes are: " , median(newcoordlist))


    #mean = sum(x[0] for x in coordinates)/len(coordinates)

    
 

