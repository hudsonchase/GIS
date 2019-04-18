# Name: Hudson Chase
# Date: 02/19/2019
# Homework 3
# 'Algorithms in GIS' - Read GEOJSON

# "D:\Downloads\states.json"

def jsonstr(filein):
    import json
    import pprint
    #filein = "D:\Downloads\states.json"
    indata = open(filein,'r')
    jsonstr = indata.read()

    geodict = json.loads(jsonstr)
    geodict.keys()
    allcoord = []
    alllat = []
    totalarea = []
    #print(geodict)
    for feature in geodict['features']:
        #print ("State Name:", feature['properties']['STATE_NAME'],"// State FIPS Code:", feature['properties']['STATE_FIPS'],"// Area:", feature['properties']['Area'], "// Polygon Coordinates:", feature['geometry']['coordinates'][0])
        print("State Name: {:20s} FIPS Code: {:<6d} State Area: {:<15f} Polygon Coordinates: {}".format(feature['properties']['STATE_NAME'], feature['properties']['STATE_FIPS'], feature['properties']['Area'],feature['geometry']['coordinates'][0]))
        test = (feature['geometry']['coordinates'])
        allcoord.append(test)
        totalarea.append(feature['properties']['Area']) 
    for feature in geodict['features']:
        test2 = (feature['geometry']['coordinates'][0])
        alllat.append(test2)
    #print (alllat)
    flattened = []
    for sublist in alllat:
        for val in sublist:
            flattened.append(val)
    #print (flattened)
    #print(totalarea)
    print("File Statistics:")
    #latlist = []
    #longlist = []
    #allcoord = []
        #test = (feature['geometry']['coordinates'])
    #allcoord.append(test)
    #print(allcoord[1:])
    print("The number of polygons is",len(allcoord),"including D.C")
    #print (totalarea)
    #print(test2)
    #print(min(x[1] for x in flattened))
    long = sorted(x[0] for x in flattened)
    lat = sorted(x[1] for x in flattened)

    print("The max longitude is:", max(x[0] for x in flattened))
    print("The min longitude is:", min(x[0] for x in flattened))
    print("The max latitude is:", max(x[1] for x in flattened))
    print("The min latitude is:", min(x[1] for x in flattened))
    print("The mean coordinates are:", sum(x[0] for x in flattened)/len(flattened), ",", sum(x[1] for x in flattened)/len(flattened) )

    def median(lst):
        n = len(lst)
        if n < 1:
                return None
        if n % 2 == 1:
                return sorted(lst)[n//2]
        else:
                return sum(sorted(lst)[n//2-1:n//2+1])/2.0

    #print(a)
    #print(lat)
    print("The median coordinates are:,", median(long), ",", median(lat))
    print("The total area of the US states is:", sum(totalarea))