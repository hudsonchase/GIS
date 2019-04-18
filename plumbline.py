class Point(object):
    """ stores the coordinates of a 2d point 
    poperties:
        x: float
        y: float
    """

    def __init__(self, x1, y1):
        self.x = float(x1)
        self.y = float(y1)

    def maybe(self,poly):
        box = poly.bbox()
        if self.x < box[0] or self.x > box[2] or self.y < box[1] or self.y > box[3]:
            return (False)
        else:
            return (True)

def pinp(xpt, ypt, xlist, ylist):

    #create a test point from xpt, ypt
    tpt = Point(xpt, ypt)

    #create a list of point objects from the coordinate lists
    li = []
    for i in range(len(xlist)):
        p = Point(xlist[i], ylist[i])
        li.append(p)

    #create poygon object
    polytest = Polygon(li)

    #check if tpt point is in the bounding box
    maybe = tpt.maybe(polytest)

    #continue if true
    if maybe:
        #reset the intersections counter to 0
        intersections = 0

    #check each segment on the perimeter for intersection
        for i in range(0,len(polytest.points)-1):

            #guarateed non left
            if polytest.points[i].x < tpt.x and polytest.points[i+1].x < tpt.x:
                continue
            #guaranteed none right
            if polytest.points[i].x > tpt.x and polytest.points[i+1].x > tpt.x:
                continue
            #guaranteed none above
            if polytest.points[i].y > tpt.y and polytest.points[i+1].y > tpt.y:
                continue
            #guaranteed intersection - straddle below
            if polytest.points[i].y < tpt.y and polytest.points[i+1].y < tpt.y:
                intersections += 1
                continue

            #must compute intersection
            slope = (polytest.points[i+1].y - polytest.points[i].y) \
                / (polytest.points[i+1].x - polytest.points[i].x)
            yint = polytest.points[1].y - slope * polytest.points[1].x
            yheight = slope * tpt.x + yint
            if yheight < tpt.y:          #< means on-line doesn't count as an intersection.
                intersections += 1
        if intersections % 2 == 1:
            return('Y')
        else:
            return('N')



class Polygon(object):
    """stores a simple polgyon point listing as a list structure properties:

        points: a list of Point Objects
    """
    def __init__(self,pts):
        self.points = pts
    def listpts(self):
        for i in self.points:
            print(i.x, i.y)
    def bbox(self):
        x = []
        y = []
        for p in self.points:
            x.append(p.x)
            y.append(p.y)
        return(min(x), min(y), max(x), max(y))


# main
import math

#create a rectangle polygon with corners at 
li = [[3,3], [3,5], [5,5], [5,3], [3,3]]
li2 = []
for i in range(len(li)):
    li2.append(Point(li[i][0],li[i][1]))

poly1 = Polygon(li2)
poly1.listpts()

box = poly1.bbox()
print(box)

ptin = Point(4,4)
ptin.maybe(poly1)

ptin = Point(1,1)
ptin.maybe(poly1)

