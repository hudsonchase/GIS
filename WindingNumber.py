# winding number code sample courtesy of Dan Sunday - orignially in C++

# test if a polygon edge passes to the left
#return is
#          > 0 if point is left of line
#          < 0 if point is right of line
#         == 0 if point is on line
def isleft(x0,y0,x1,y1,x2,y2):
    return (x1-x0) * (y2-y0) - (x2-x0) * (y1-y0)


def winding(xpt,ypt,x, y):  
    #start a counter for the winding number
    wnum = 0
    #test all edges of the polygon
    for i in range(0,len(x)-1):
        #line passes the botttom to top, so left counts only  (UP LEFT = +1)
        if y[i] <= ypt: 
            if y[i+1] > ypt: 
                if isleft(x[i], y[i], x[i+1], y[i+1],xpt,ypt) > 0:
                    wnum += 1
        else:
        # line passes going down, so must be on right to counter the one going up (DOWN RIGHT = -1)
            if y[i+1] <= ypt:   
                if isleft(x[i], y[i], x[i+1], y[i+1],xpt,ypt) < 0:
                    wnum -= 1
        if wnum != 0:
            r = 'Y'
        else:
            r = ' '
    return r



