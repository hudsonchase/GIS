def add4(x):
    x = x + 4
    print(x)

#countdown
def recurse(x):
    print(x)
    x = x - 1
    if x > 0:
        recurse(x)

#odd or even
lambda x: True if x % 2 == 0 else False

# dice counter
def doubles():
    import random
    #set initial condition variable for the while iteration before the iteration
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    count = 1
    while die1 != die2:
        print("Not Doubles", die1, die2)
        #set next while condition variables
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        count += 1
    print("Rolled a double", die1, "....on roll....", count)

def whiCountdown(n):
    while n > 0:
        print (n)
        n -= 1
    print("blastoff!!!")


num = 0
while num != 99:
    num = int(input("Enter a number: "))
    print (num)

while True:
    num = int(input("Enter a number: "))
    if num == 99:
        break
    print (num)

for x in range(3,6):
    print(x, 'is larger than')
    for y in range (1,x):
        print(y)

for n in range (2,25):
    for x in range (2,n):
        if n % x == 0:
            print (n, "equals", x, "*", int(n/x))
            break
    else:
        print(n, " is a prime number")

def isPrime(num):
    count = 0
    for n in range (2,num):
        for x in range (2,n):
            if n % x == 0:
                print (n, "equals", x, "*", int(n/x))
                break
        else:
            print(n, " is a prime number")
            count += 1
    print(count, " prime number found below", num)

def iguess():
    import random
    num = random.randint(0,1024)
    guess = -1
    while guess != num:
        guess = int(input("Enter your guess > "))
        if guess > num:
            print ("Lower")
        elif guess < num:
            print ("Higher")
        else:
            print("Congratulations - you got it!!!", num)

def uguess():
    import random
    guess = random.randint(0,1024)
    num = random.randint(0,1024)
    while guess != num:
        if guess > num:
            print ("Lower")
            guess -= 1
        elif guess < num:
            print ("Higher")
            guess += 1   
    print("Congratulations - you got it!!!", num)

def uguess2(maxnum):
    import random
    tries = 1
    guess = maxnum // 2
    step = guess // 2
    num = random.randint(0,maxnum)
    while guess != num:
        tries += 1
        if guess > num:
            print ("Lower than", guess)
            guess -= step
            step = max(step // 2, 1)
        elif guess < num:
            print ("Higher than", guess)
            guess += step
            step = max(step // 2, 1)
    print("Congratulations - you got it!!!", num, " in", tries, " tries")

fruit = "grape"
letter1 = fruit[1]
print(letter1)

s = "Monty Python"
s[0:5]

def piglatin(word):
    if word[0] in 'aeiou':
        return word + "way"
    else:
        return word[1:len(word)] + word[0] + 'ay'
 
def findlet(letter,word):
    if letter in word:
        print ("Yes, it's there")
    else:
        print ("No it's not")

def findlet(letter, word):
    count = 0
    for let in word:
        if let == letter:
            count += 1
    print("There are ", count, letter, 'in the word', word)

def locate(let, word):
    start = 0
    index = 0 

    while start < len(word):
        index = word.find(let,start)
        print ("found an", let, "in position", index)
        start = index + 1 

li = [1, 321, 23, 3, 5, 65]
for i in li:
    i + [i+1]

def acummlist(inlist):
    sum = 0
    accumulation = []
    for i in inlist:
        sum = sum + i
        accumulation.append(sum)
    print (inlist, accumulation)

def convert(instring):
    li = instring.split()
    linew = sorted(li)
    delimiter = ' '
    outstring = delimiter.join(linew)
    print(outstring)

def has_dups(inlist):
    newlist = []
    for i in inlist:
        if inlist.count(i) > 1:
            if i not in newlist:
                newlist.append(i)                
    return newlist

def repeat(inlist):
    w = []
    words = inlist.split()
    for word in inlist:
        count = words.count(word)
        if word not in w:
            w.append(word)
            print(word,count)

def repeat3(para):
    w = []
    out = []
    words = para.split()
    for word in words:
        count = words.count(word)
        if word not in w:
            w.append(word)
            out.append([word, count])
    outs = sorted(out)
    for w in outs:
        print(w)

#initialize list of lists
points = [[0 for row in range(2)] for col in range(5)]
points
[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

#print 8 index of y
print(points2[8][1])
60

#list of y values
print ([points2[i][1] for i in range(len(points2))])
#list of x values
print ([points2[i][0] for i in range(len(points2))])

data = dict()
type(data)

def statistics():
    rolls = []
    import random
    for i in range (0,100):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        roll = d1 + d2
        rolls.append(roll)
    li = sorted(rolls)
    for i in range(2,13):
        num = li.count(i)
        print(i, num, "*" * num, float((num/len(li) * 100),2),'%')
    return (min(li), max(li), sum(li)/len(li), li[len(li)//2])

print ("{0:<6d}|{1:>6d}|{2:^6d}|".format(58,58,58))
#58    |    58|  58  |
print ("{0:<6d}|{1:>6d}|{2:^6d}|".format(58,58,58))
#58    |    58|  58  |
print("{0:+5.2f}    {1:+5.2f}".format(58.6, -58.6))
#+58.60    -58.60
print ("{0:-^10s}".format('58'))
#----58----

print ("{0:06d}     {1:8b}".format(58, 58))
#000058       111010
print ("{0:06d} {1:e}   {2:f}   {3:g}".format(58, 58,58,58))
#000058 5.800000e+01   58.000000   58
print ("{0:06d} {1:e}   {2:f}   {3:%}".format(58, 58,58,58))
#000058 5.800000e+01   58.000000   5800.000000%
print ("{0:06d} {1:e}   {2:f}   {0:%}".format(58, 58,58,58))
#000058 5.800000e+01   58.000000   5800.000000%
print ("{0:06d} {1:e}   {2:f}   {1:%}".format(58, 58,58,58))
#000058 5.800000e+01   58.000000   5800.000000%

def cubeprint():
    for i in range(0,26):
        print("{0:6d}{1:6d}{2:6d}".format(i, i**2, i**3))

def cubeprint2():
    import math
    for i in range(0,26):
        print("{0:3d}{1:10.3f}{2:10.3f}".format(i, i**.5, i**.333))

for i in range(0,256):
    print('The Binary code of {0:g} is {1:8b}'.format(i,i))

print('This is the first line and \nThis is the second. This line has a \ttab in it.')
#This is the first line and 
#This is the second. This line has a 	tab in it

def readcsv():
    infile = open('D:/a/VACities.csv','r')
    li = []
    for fields in csv.reader(infile, delimiter = ','):
        li.append(fields)
    infile.close()
    for i in li:
        print(i[6])

def writebin():
    outfile = open('D:/a/testb.txt', 'wb')
    import struct
    #write some binary integers
    for x in range(65,123):
        outstr = struct.pack('i',x)
        outfile.write(outstr)
    outfile.close()

def readbin():
    infile = open('D:/a/testb.txt','rb')
    import struct
    #read them back in 
    instr = infile.read(4)
    #end of file check - while used as we do not know 
    #how many times we will read from the file.
    while len(instr) > 0:
        i = struct.unpack('i', instr)
        print(i[0])
        instr = infile.read(4)
    infile.close()

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
    #print(geodict)
    for feature in geodict['features']:
        #print ("State Name:", feature['properties']['STATE_NAME'],"// State FIPS Code:", feature['properties']['STATE_FIPS'],"// Area:", feature['properties']['Area'], "// Polygon Coordinates:", feature['geometry']['coordinates'][0])
        print("State Name: {:20s} FIPS Code: {:<6d} State Area: {:<15f} Polygon Coordinates: {}".format(feature['properties']['STATE_NAME'], feature['properties']['STATE_FIPS'], feature['properties']['Area'],feature['geometry']['coordinates'][0]))
        test = (feature['geometry']['coordinates'])
        allcoord.append(test)
    for feature in geodict['features']:
        test2 = (feature['geometry']['coordinates'][0])
        alllat.append(test2)
    #print (alllat)
    flattened = []
    for sublist in alllat:
        for val in sublist:
            flattened.append(val)
    #print (flattened)
    print("File Statistics:")
    #latlist = []
    #longlist = []
    #allcoord = []
        #test = (feature['geometry']['coordinates'])
    #allcoord.append(test)
    #print(allcoord[1:])
    print("The number of polygons is",len(allcoord),"including D.C")
    
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

def drawlines():
    import random
    win = graphics.GraphWin("line drawing", 500, 500,True)
    p1 = graphics.Point(random.randint(0,500),random.randint(0,500))
    for i in range(0,51):
        p2 = graphics.Point(random.randint(0,500), random.randint(0,500))
        line = graphics.Line(p1,p2)
        line.draw(win)
        p1=p2
    win.getMouse()
    win.close()

import pyshp

import shapefile as shp  # Requires the pyshp package
import matplotlib.pyplot as plt

sf = shp.Reader("D:/VSProjects/ShapeFileReader/areatestpolys.shp")

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.gca (projection='3d')
x = np.arange(0,3612,1)
y = np.arange(3612, 0, -1)
X,Y = np.meshgrid(x,y)
Z = elev.reshape(3612,3612)
surf = ax.plot_surface(Y,X,Z, cmap = cm.coolwarm)
plt.show()


e = np.fromfile("D:\VSProjects\yosemite1m.flt", 'f')
# 3612 came from HDR file
e2 = e.reshape(3612,3612)
plt.imshow(e2, cmap='terrain')
plt.show()

data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data)
df
#        0   1
#0    Alex  10
#1     Bob  12
#2  Clarke  13
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data,columns=['Name', 'Age'])
df
#     Name  Age
#0    Alex   10
#1     Bob   12
#2  Clarke   13
data = {'Name':['Tom','Jack','Steve','Ricky'], 'Age':[28,34,29,42]}
df = pd.DataFrame(data)
df
#    Name  Age
#0    Tom   28
#1   Jack   34
#2  Steve   29
#3  Ricky   42
print(df['Name'])
#0      Tom
#1     Jack
#2    Steve
#3    Ricky
Name: Name, dtype: object
print(df['Name'][2])
Steve
df['State'] = pd.Series(['VA','NC','VA','SC'])
df
#    Name  Age State
#0    Tom   28    VA
#1   Jack   34    NC
#2  Steve   29    VA
#3  Ricky   42    SC
df3 = pd.DataFrame([['Susan', 43, 'TN']], index = [4], columns=['Name', 'Age','State'])
dd = df.append(df3)
dd
#    Name  Age State
#0    Tom   28    VA
#1   Jack   34    NC
#2  Steve   29    VA
#3  Ricky   42    SC
#4  Susan   43    TN
dd.drop(0)
#    Name  Age State
#1   Jack   34    NC
#2  Steve   29    VA
#3  Ricky   42    SC
#4  Susan   43    TN

#'D:\VSProjects'

july = df.loc[df['Month']==7]

y = df.groupby('Month').mean()

tmax = df.loc[21170:, ['TMAX','Month']]
tmax
#       TMAX  Month
#21170  39.0     12
#21171  44.0     12
#21172  47.0     12
#21173  37.0     12
#21174  49.0     12
#21175  51.0     12
#21176  56.0     12


import random
for i in range(0,50):
    x = random.randint(0,100)
    y = random.randint(0,100)
    pts.append([x,y])

points = np.array(pts)

from scipy.spatial import Delaunay
tri = Delaunay(points)
plt.triplot(points[:,0], points[:,1], tri.simplices)
#[<matplotlib.lines.Line2D object at 0x0000022C697ED358>, <matplotlib.lines.Line2D object at 0x0000022C697ED4A8>]
plt.plot(points[:,0], points[:,1], 'o')
#[<matplotlib.lines.Line2D object at 0x0000022C697ED208>]
plt.show()

def plotit(data):
    import scipy
    from scipy import stats
    import matplotlib.pyplot as plt
    x = data['TMIN']
    y = data['TMAX']
    st = stats.linregress(x,y)
    r2 = st[2]**2

def plotit(data):
    import scipy
    from scipy import stats
    import matplotlib.pyplot as plt
    x = data['TMIN']
    y = data['TMAX']
    st = stats.linregress(x,y)
    r2 = st[2]**2
    data.plotit.scatter(x='TMIN', y = 'TMAX')
    xmin = data['TMIN'].min()
    xmax = data['TMAX'].max()
    step = (xmax-xmin)/10
    xi = np.arange(xmin, xmax, step)
    line = st[0] * xi + st[1]
    plt.plot(xi,line)
    equation = '{0:7.3f} X + {1:7.3f} \n R2 = {2:5.3f}'.format(st[0], st[1], r2)
    plt.title(equation)
    plt.show()

class Point(object):
    """contains a 2D point object.
    attributes" x: float y: float """

    def __init__(self, x1, y1):
        self.x = float(x1)
        self.y = float(y1)

class city(Point):
    def __init__(self,x,y,name):
        Point.__init__(self,x,y)
        self.name = name

class student(object):
    stucount = 0
    def __init__(self,name,grade):
        self.name = str(name)
        self.grade = str(grade)
        student.stucount += 1
    def getCount(self):
        print("the current number of students is ", student.stucount)
    def listStudent(self):
        print("Name: ", self.name, "      Grade: ", self.grade)

class student(object):
    stucount = 0
    slist=[]
    def __init__(self,name,grade):
        self.name = str(name)
        self.grade = str(grade)
        student.stucount += 1
        student.slist.append(self)
    def getCount(self):
        print("the current number of students is ", student.stucount)
    def listStudent(self):
        print("Name: ", self.name, "      Grade: ", self.grade)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def checker():
    a = arcpy.ListFeatureClasses()
    srlist= []
    for e in a:
        sr = arcpy.Describe(e)
        print("{0:20s}    {1:50s}".format(e,sr.spatialreference.name))
        srlist.append(sr.spatialreference.name)
    r = histogram(srlist)
    return r

def buff(layer):
    if arcpy.Exists(layer):
        return arcpy.Buffer_analysis(layer,layer+'_buff',"1 mile")
    else:
        print(layer, "does not exist, cannot buffer")

def describeem():
    rlist = arcpy.ListRasters()
    for r in rlist:
        desc = arcpy.Describe(r) 
        print("This is info for", r)
        print(desc.basename)
        print(desc.format)
        print(desc.dataType)
        print(desc.Extension)
        print(desc.spatialReference.name)
        print(desc.bandCount)
        if desc.bandcount == 1:
                print("mean cell height is ", desc.meanCellHeight)
                print("mean cell width is", desc.meanCellWidth)
                print("number of rows is ", desc.height)
                print("number of columns is  ", desc.width)
                print("no data value is ", desc.noDataValue)
                print('****************')
        else:
                desc = arcpy.Describe(r+ '/band_1') 
                print("mean cell height is ", desc.meanCellHeight)
                print("mean cell width is", desc.meanCellWidth)
                print("number of rows is ", desc.height)
                print("number of columns is  ", desc.width)
                print("no data value is ", desc.noDataValue)
                print('****************')

#solar home suitability
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


