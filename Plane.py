
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Parametrization
t = np.linspace(-4 * np.pi, 2 * np.pi, 50)
s = np.linspace(-4 * np.pi, 2 * np.pi, 50)
t, s = np.meshgrid(t, s)
x0, y0, z0, r = [1, 2, 0, 1]
a, b, c = [-2, -1, 1]
x = x0 + t*a
y = y0 + t*b
z = z0 + s*c #3d plane
#z = z0 + t*c #3d line

def plotter(E, A):
    #plt.contour(x, y, z) # points of surface and z=0 plane
    plt.contour(x, y, z, 15) # more levels
    # Axes
    fig = plt.figure('Plot and Contour plot')
    #ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca(projection='3d')
    h = ax.plot_surface(x, y, z, cmap = cm.tab20c, edgecolor = 'k') #gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, Accent, hsv
    fig.colorbar(h)
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax.set_title('Plane', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    plt.show()
plotter(0, 45)