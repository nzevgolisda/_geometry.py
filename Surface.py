

import numpy as np
import mpl_toolkits.mplot3d as Axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
# Parametrization
f = lambda x, y: np.sin(x)*np.cos(y)
t = np.linspace(-0.5*np.pi, 1.5*np.pi, 80)
s = np.linspace(-0.5*np.pi, 1.5*np.pi, 80)
x, y = np.meshgrid(t, s)
z = f(x, y)
def plotter(E, A):
    plt.contour(x, y, z, 15)
    fig = plt.figure('Plot and Contour plot')
    ax = fig.add_subplot(111, projection='3d')
    h = ax.plot_surface(x, y, z, cmap = cm.plasma, edgecolor = 'k')
    fig.colorbar(h)
    ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax.set_title('Surface and Contour of F = sin(x)*cos(y)', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    plt.show()
plotter(0, 45)