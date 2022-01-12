
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
from matplotlib import cm

# Parametrization
t = np.linspace(0 * np.pi, 2 * np.pi, 200)
s = np.linspace(-2 * np.pi, 2 * np.pi, 200)
t, s = np.meshgrid(t, s)
x0, y0, z0, r = [0, 0, 0, 1]
x = x0 + s*np.cos(t)
y = y0 + s*np.sin(t)
#z = z0 + s #Cone
z = z0 + t #Helix

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
    #ax.set_title('Cone', fontweight = 'bold', fontsize = 16)
    ax.set_title('Helix', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    h = ax.plot_surface(x, y, z, cmap = cm.tab20c, edgecolor = 'k')
    fig.colorbar(h)
    fig.tight_layout()
    #a = plt.gca()
    #plt.axis('off')
plotter(0, 45)

