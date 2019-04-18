import struct, math, csv, graphics, random, plumbline as p



#main program

file_in = open("D:/VSProjects/tracts2.shp", "rb")
s = file_in.name
path = s[0:s.rfind('/')]
file_out = open(path + '/tracts2test2.csv','w')
dataWrite = csv.writer(file_out, delimiter = ",", lineterminator = "\n")
dataWrite.writerow(["Polygon", "Perimeter", "Area", "InPoly", "TestX", "TestY"])

xtest = float(input("Enter the UTM easting to test: "))
ytest = float(input("Enter the UTM northing to test: "))


#decode needed parts from header
datain = file_in.read(28)
vals = struct.unpack(">7i",datain)
datain = file_in.read(72)
vals2 = struct.unpack("<2i8d",datain)

#set up for graphics
win = graphics.GraphWin("Shapefile Plot", 500,500,True)
#scale the graphics window
win.setCoords(vals2[2],vals2[3],vals2[4],vals2[5])


#check to be sure a polygon file
if vals2[1] == 5:
#read a record header (big endian)
    datain = file_in.read(8)
    while len(datain) != 0:
        #decode the polygon header
        vals3= struct.unpack(">2i",datain)
        #read the shape type      
        datain = file_in.read(4)
        stype = struct.unpack("i",datain)
        #read the bounding box for polygon
        datain = file_in.read(32)
        xmin, ymin, xmax, ymax = struct.unpack("4d",datain)
        #read the number of parts and the number of points
        datain = file_in.read(8)
        nparts, npts = struct.unpack("2i",datain)

        #read the points into a blank list
        x = []
        y = []
        datain = file_in.read(4)
        skip4 = struct.unpack('i', datain)
        for i in range(0,npts):
            datain = file_in.read(16)
            tempx, tempy = struct.unpack("dd",datain)
            x.append(tempx)
            y.append(tempy)
        #    print tempx, tempy

        #compute the perimeter and area for the polygon
        length = 0.0
        sum1 = 0.0
        sum2 = 0.0
        
        for i in range(0,npts-1):
            length = length + math.sqrt((x[i] - x[i+1])**2 + (y[i] - y[i+1])**2)
            sum1 = sum1 + (x[i] * y[i+1])
            sum2 = sum2 + (y[i] * x[i+1])

        length = length / 1609.0
        area = abs((sum1-sum2)/2.0)
        area = area /1609**2

        #compute point in polygon
        inpoly = p.pinp(xtest,ytest,x,y)

        #report to the user (and you for testing)
        if inpoly == 'Y':
            print("Point ({0:8.0f}, {1:8.0f}) found in polygon {2:3d}"\
                .format(xtest,ytest,vals3[0]-1))

        #report the information on the polygon
        dataWrite.writerow([vals3[0] -1, length, area, inpoly, xtest, ytest])

        #draw the polygon - need to scale the coordinates first as the window is in pixels, not UTM
        #use setCoords and the bounding box (for now)

        li = []
        for i in range(len(x)-1):
            pt1 = graphics.Point(x[i],y[i])
            li.append(pt1)
        
        poly = graphics.Polygon(li)
        poly.setFill(graphics.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        poly.draw(win)

        #add the pinp drawing
        tp = graphics.Point(xtest,ytest)
        tc = graphics.Circle(tp, 200)
        tc.setOutline("white")
        tc.setFill("black")
        tc.draw(win)
               
        #read the next record header (big endian) - done here to test for the End of File - will be len = 0 when done
        datain = file_in.read(8)
   
file_in.close()
file_out.close()












#import struct, math, csv, graphics, random

#def distance(xpt1, ypt1, xpt2, ypt2):
#    dx = xpt2 - xpt1
#    dy = ypt2 - ypt1
#    dsq = dx**2 + dy**2
#    result = math.sqrt(dsq)
#    return result

##file_in = open(input("Enter the Shapefilename (.shp): "), "rb")
#file_in = open("D:/VSProjects/tracts2.shp",'rb')
#file_out = open("D:/VSProjects/ShapeFileReader/tractstest.csv", "w")
#dataWrite = csv.writer(file_out, delimiter = ",", lineterminator = "\n")
#dataWrite.writerow(["Polygon", "Perimeter", "Area"])


##decode the main file header----integers 4 bytes, if you have 7 of them you have 28 bytes
#datain = file_in.read(28)
#vals = struct.unpack(">7i",datain)
#datain = file_in.read(72)
#vals2 = struct.unpack("<2i8d",datain)

##get correct ration range of x and y values
#ratio = (vals2[4]-vals2[2])/(vals2[5]-vals2[3])

##set up the graphics 
#win = graphics.GraphWin("Shapefile Plot", (500*ratio),500,True)

##Scale to the coordinates of the shapefile
#win.setCoords(vals2[2], vals2[3], vals2[4], vals2[5])

##doubles are 8 bytes --- check to be sure a polygon file
#if vals2[1] == 5:

##read a record header (big endian)
#    datain = file_in.read(8)
#    while len(datain) != 0:
#        #decode the polygon header
#        vals3 = struct.unpack(">2i",datain)
#        #read the shape type
#        datain = file_in.read(4)
#        stype = struct.unpack("i", datain)
#        #read the bounding box for polygon
#        datain = file_in.read(32)
#        xmin, ymin, xmax, ymax = struct.unpack("4d", datain)
#        #read the number of parts and the number of points
#        datain = file_in.read(8)
#        nparts, npts = struct.unpack("2i", datain)
    
#        #read the points into lists
#        x = []
#        y = []
    
#        #read the part start code 
#        datain = file_in.read(4)

#        #for iteration to read "npts" points
#        for i in range(0,npts):
#            datain = file_in.read(16)
#            tempx, tempy = struct.unpack("dd",datain)
#            #append the decoded numbers to list
#            x.append(tempx)
#            y.append(tempy)
    
#        #iteration to calculate the perimeter
#        length = 0.0
    
#        for i in range(0,npts-1):
#            length = length + distance(x[i],y[i], x[i+1], y[i+1])
#        length = length/1609.0
    
#        #compute the polygon area from coordinates
#        sum1 = 0.0
#        sum2 = 0.0
#        for i in range(0,npts-1):
#            sum1 = sum1 + (x[i]  * y[i+1])
#            sum2 = sum2 + (y[i]  * x[i+1])
#        area = abs((sum1-sum2)/2.0)
#        area  = area / 1609**2

#        #report the information on the polygon
#        dataWrite.writerow([vals3[0]-1, length, area])

#        #draw polygon
#        li = []
#        for i in range(0,npts-1):
#            pt1 = graphics.Point(x[i],y[i])
#            li.append(pt1)
#            #pt2 = graphics.Point(x[i+1],y[i+1])
#            #ln = graphics.Line(pt1,pt2)
#        poly = graphics.Polygon(li)
#        poly.setFill(graphics.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#        poly.draw(win)
#            #ln.draw(win)

#        datain = file_in.read(8)
#win.getMouse()
#win.close()
#file_in.close()
#file_out.close()

#    #works exactly like pyshp

