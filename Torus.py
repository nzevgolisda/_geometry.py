
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d as Axes3d

# Parametrization
t = np.linspace(0 * np.pi, 2 * np.pi, 40)
s = np.linspace(0 * np.pi, 2 * np.pi, 30)
t, s = np.meshgrid(t, s)
x0, y0, z0, r, r1 = [0, 0, 0, 1, 1.5]
x = x0 + (r1 + r * np.cos(t))*np.cos(s)
y = y0 + (r1 + r * np.cos(t))*np.sin(s)
z = z0 + (r1 + r * np.sin(t))

def plotter(E, A):
    #plt.contour(x, y, z) # points of surface and z=0 plane
    #plt.contour(x, y, z, 15) # more levels
    # Axes
    fig = plt.figure('Plot and Contour plot')
    ax = fig.add_subplot(111, projection='3d')
    #ax = fig.gca(projection='3d')
    h = ax.plot_surface(x, y, z, cmap = cm.tab20c, edgecolor = 'k')
    #cmap = gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, 
    # Accent, hsv | edgecolor = k, p, r, qfig.colorbar(h)
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax.set_title('Torus', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    plt.show()
plotter(0, 45)