def tindraw(n):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from scipy.spatial import Delaunay
    import random
    #open the yosemite file
    e = np.fromfile('D:/vsprojects/yosemite1m.flt','f')
    elev = e.reshape(3612,3612)
    #select a sample of the points from the NED data
    
    pts=[]
    for i in range(0,n):
        xt = random.randint(0,3162)
        yt = random.randint(0,3162)
        zt = elev[xt][yt]
        pts.append([xt,yt,zt])
    points=np.array(pts)
    x = np.array(points[:,0])
    y = np.array(points[:,1])
    z = np.array(points[:,2])
       
    # Triangulate parameter space to determine the triangles
    tri = Delaunay(pts)

    #draw the TIN
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0

    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # The triangles in parameter space determine which x, y, z points are
    # connected by an edge

    ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap=plt.cm.terrain)
    plt.show()
