import graphics
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
drawlines(win)

