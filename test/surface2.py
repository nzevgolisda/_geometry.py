

## Contour Plot
#X, Y = np.mgrid[-2:2:100j, -2:2:100j]
#Z = X*np.exp(-(X**2 + Y**2))
#
## Vector Field
#Y, X = np.mgrid[-2:2:20j, -2:2:20j]
#U =(1 - 2*(X**2))*np.exp(-((X**2)+(Y**2)))
##V = -2*X*Y*np.exp(-((X**2)+(Y**2)))

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
from matplotlib import cm

# Parametrization
t = np.linspace(0 * np.pi, 2 * np.pi, 20)
s = np.linspace(0 * np.pi, 1 * np.pi, 20)
t, s = np.meshgrid(t, s)
x0, y0, z0 = [0, 0, 0]
a, b, c, r = [1, 1, 1, 1]
x = x0 + a*r * np.cos(t)*np.sin(s)
y = y0 + b*r * np.sin(t)*np.sin(s)
z = z0 + c*r * np.cos(s)

#ax.plot(x, y, z)
##np.mgrid[-2:2:100j, -2:2:100j]
#t = np.linspace(-2, 2, 100)
#s = np.linspace(-2, 2, 100)
#t, s = np.meshgrid(t, s)
#x = t
#y = s
#z = x*np.exp(-(x**2 + y**2))
#
def plotter(E, A):
    #plt.contour(x, y, z) # points of surface and z=0 plane
    plt.contour(x, y, z, 0) # more levels
    # Axes
    fig = plt.figure('Plot and Contour plot')
    #ax = fig.add_subplot(111,aspect='equal')
    #ax = fig.add_subplot(111,aspect=1.0)
    #ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(111, aspect='equal', projection='3d')
    ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z), []))  # aspect ratio is 1:1:1 in data space
    ax.set_aspect('auto')
    plt.axes().set_aspect('auto')
    fig.tight_layout()
    #ax = fig.gca(projection='3d')
    h = ax.plot_surface(x, y, z, cmap = cm.plasma, edgecolor = 'k')
    #cmap = gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, 
    # Accent, hsv | edgecolor = k, p, r, q
    fig.colorbar(h)
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax.set_title('Sphere x**2 + y**2 + z**2 = 1', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    
    fig.tight_layout()
    plt.show()
plotter(0, 45)




