
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d as Axes3d

# Parametrization
t = np.linspace(-2 * np.pi, 2 * np.pi, 20)
s = np.linspace(-2 * np.pi, 2 * np.pi, 20)
t, s = np.meshgrid(t, s)
x0, y0, z0 = [0, 0, 0]
a, b, c = [1, 1, 1]
x = x0 + t*a
y = y0 + t*b
z = z0 + s*c #3d plane
#z = z0 + t*c #3d line

def plotter(E, A):
    #plt.contour(x, y, z, 15) # projected points of surface at z=0 plane
    fig = plt.figure('Plot and Contour plot') #fig category
    ax = fig.add_subplot(111, projection='3d')
    setAxes(fig, ax, E, A) # fig axes from E, A point of view
    plt.show()

def setAxes(fig, ax, E, A):
    #cmap = gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, Accent, hsv | edgecolor = k, p, r, q
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax.set_title('Plane: x + y + z = 0', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    h = ax.plot_surface(x, y, z, cmap = cm.tab20c, edgecolor = 'k')
    fig.colorbar(h)
    fig.tight_layout()
    a = plt.gca()
    plt.axis('off')
plotter(0, 45)