



import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
from matplotlib import cm

# Parametrization
t = np.linspace(0 * np.pi, 2 * np.pi, 20)
s = np.linspace(0 * np.pi, 2 * np.pi, 20)
t, s = np.meshgrid(t, s)
x = t**3 -s*t + 2
y = s-t
z = s+t


def plotter(E, A):
    #plt.contour(x, y, z) # points of surface and z=0 plane
    plt.contour(x, y, z, 15) # more levels
    # Axes
    fig = plt.figure('Plot and Contour plot')
    ax = fig.add_subplot(111, projection='3d')
    

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




