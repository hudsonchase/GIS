class state(object):
    """state is an object a that contains a state database
    properties:
        name: string
        fips: integer
        area: float
        centerx: float
        centery: float

    methods:
        __init__: create an instance of a state and compute the centroid location
        from the outline passed in

        distance: compute the Manhattan distance between state centroids in miles.
        """

    statenum = 0
    statelist = []

    def __init__(self,name,fips,area,coords):
        self.name = str(name)
        self.fips = int(fips)
        self.area = float(area)
        state.statelist.append(self)
        state.statenum += 1

        x = [coords[0][j][0] for j in range(len(coords[0]))]
        y = [coords[0][j][1] for j in range(len(coords[0]))]
        
        self.centerx = sum(x)/len(x)
        self.centery = sum(y)/len(y)

    def distance(self, other):
        ew = self.centerx - other.centerx
        ns = self.centery - other.centery
       
        return (ew/1609, ns/1609)

#main

#read the json data from the disk
import json
filein = open('D:/VSProjects/test.json', 'r')
data = filein.read()

#convert to a dictionary
gdict = json.loads(data)

#load a list of state objects with the json data
states = []
for feature in gdict['features']:
    statename = feature['properties']['STATE_NAME']
    statefips = feature['properties']['STATE_FIPS']
    statearea = feature['properties']['Area']
    coords = feature['geometry']['coordinates']
    st = state(statename, statefips, statearea, coords)
    states.append(st)

for i in range(len(states)):
    d = states[0].distance(states[i])
    print("{0:25s} is {1:8.2f} miles east and {2:8.2f} miles north of {3:25s}"\
        .format(states[0].name,d[0],d[1],states[i].name))

import numpy as np

for i in range(len(states)):
    print()
    for j in range(len(states)):
        e,n = states[i].distance(states[j])
        print("{0:5.0f}  ".format(e), end='')
#test1 = np.array(d[0])
#z = numpy.array()
