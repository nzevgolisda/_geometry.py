
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d as Axes3d
from numpy.core.function_base import linspace

# Parametrization
t = np.linspace(0, 1 * np.pi, 40) # Mobius strip (athanasopoulos)
s = np.linspace(0, 2 * np.pi, 40) # Mobius strip (athanasopoulos)
#t = np.linspace(0, 2 * np.pi, 40) # Klein bottle (wiki)
#s = np.linspace(0, 2 * np.pi, 40) # Klein bottle (wiki)
t, s = np.meshgrid(t, s)
#a, b = [0.5, 2**0.5] # a>2 # Mobius strip
#x = np.cos(t)*(np.cos(a*t)*(b+np.cos(s))+ np.sin(a*t)*np.sin(s)*np.cos(s)) # Mobius strip (athanasopoulos)
#y = np.sin(t)*(np.cos(a*t)*(b+np.cos(s))+ np.sin(a*t)*np.sin(s)*np.cos(s)) # Mobius strip (athanasopoulos)
#z = -np.sin(a*t)*(b+np.cos(s))+ np.cos(a*t)*np.sin(s)*np.cos(2*s) # Mobius strip (athanasopoulos)


a, b = [3, 6, 5, 2/15, 0.5] # a>2  # Klein bottle (wiki)
x = (a - s*np.sin(b*t)*np.sin(b*t))*np.sin(t)  # Klein bottle (wiki)
y = (a - s*np.cos(b*t)*np.sin(b*t))*np.cos(t)  # Klein bottle (wiki)
z = (s)*np.cos(b*t)  # Klein bottle (wiki)

def plotter(E, A):
    #plt.contour(x, y, z) # points of surface and z=0 plane
    plt.contour(x, y, z, 15) # more levels
    # Axes
    fig = plt.figure('Plot and Contour plot')
    ax = fig.add_subplot(111, projection='3d')
    #ax = fig.gca(projection='3d')
    h = ax.plot_surface(x, y, z, cmap = cm.viridis, edgecolor = 'k')
    #cmap = gist_stern, tab20c, PuBuGn, tab20, terrain, gnuplot, viridis, cubehelix, Dark2, flag, 
    # Accent, hsv | edgecolor = k, p, r, qfig.colorbar(h)
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    #ax.set_title('Mobius strip', fontweight = 'bold', fontsize = 16)
    ax.set_title('Klein Bottle', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    plt.show()
plotter(0, 45)