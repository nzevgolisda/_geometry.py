##
##
##import numpy as np
##import mpl_toolkits.mplot3d as Axes3d
##from matplotlib import cm
##import matplotlib.pyplot as plt
### Parametrization
##f = lambda x, y: x**2 -y**2
##g = lambda x, y: x**2 +y**2
##j = lambda x, y: (x/4)**2 +(y)**2
### Parametrization
##t = np.linspace(-2 * np.pi, 2 * np.pi, 20)
##s = np.linspace(-2 * np.pi, 2 * np.pi, 20)
##t, s = np.meshgrid(t, s)
##x = t
##y = s
###z = g(t, s) #hyperboloid
##z = j(t, s) #ellipsoid
###z = f(t, s) #paraboloid
##
##def plotter(E, A):
##    #plt.contour(x, y, z) # points of surface and z=0 plane
##    #plt.contour(x, y, z, 15) # more levels
##    # Axes
##    fig = plt.figure('Plot and Contour plot')
##    ax = fig.add_subplot(111, projection='3d')
##    #ax = fig.gca(projection='3d')
##    h = ax.plot_surface(x, y, z, cmap = cm.PuBuGn, edgecolor = 'k') #gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, Accent, hsv
##    fig.colorbar(h)
##    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
##    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
##    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
##    ax.set_title('Plane', fontweight = 'bold', fontsize = 16)
##    ax.view_init(elev=E, azim=A)
##    plt.show()
##plotter(0, 45)
##
##





import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
from matplotlib import cm

# Parametrization
t = np.linspace(0 * np.pi, 2 * np.pi, 50)
s = np.linspace(0 * np.pi, 1 * np.pi, 50)
t, s = np.meshgrid(t, s)
x0, y0, z0, r = [0, 0, 0, 1]
a, b, c = [3, 2, 5]
x = x0 + a * r * np.cos(t)*np.sin(s)
y = y0 + b * r * np.sin(t)*np.sin(s)
z = z0 + c * r * np.cos(s)


def plotter(E, A):
    #plt.contour(x, y, z) # points of surface and z=0 plane
    #plt.contour(x, y, z, 15) # more levels
    # Axes
    fig = plt.figure('Plot and Contour plot')
    ax = fig.add_subplot(111, projection='3d')
    #ax = fig.gca(projection='3d')
    h = ax.plot_surface(x, y, z, cmap = cm.tab20c, edgecolor = 'k')    
    #cmap = gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, 
    # Accent, hsv | edgecolor = k, p, r, q
    fig.colorbar(h)
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax.set_title('Ellipsoid (x/3)**2 + (y/2)**2 +(z/3**2) = 1', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    plt.show()
plotter(0, 45)

# Axes  
fig = plt.figure('Parametric Surfaces')
ax = fig.add_subplot(111, projection='3d')
h = ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = 'c')
fig.colorbar(h)
ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
ax.set_title('Conics', fontweight = 'bold', fontsize = 16)