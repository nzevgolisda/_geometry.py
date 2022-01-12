

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d as Axes3d
from numpy.core.function_base import linspace

# Parametrization
t = np.linspace(0, 1 * np.pi, 80) # Klein bottle (wiki)
s = np.linspace(0, 2 * np.pi, 80) # Klein bottle (wiki)
#t = np.linspace(0, 2 * np.pi, 40) # Mobius strip (athanasopoulos)
#s = np.linspace(0, 2 * np.pi, 40) # Mobius strip (athanasopoulos)
t, s = np.meshgrid(t, s)
#a, b = [0.5, 2**0.5] # a>2 # Mobius strip
#x = np.cos(t)*(np.cos(a*t)*(b+np.cos(s))+ np.sin(a*t)*np.sin(s)*np.cos(s)) # Mobius strip (athanasopoulos)
#y = np.sin(t)*(np.cos(a*t)*(b+np.cos(s))+ np.sin(a*t)*np.sin(s)*np.cos(s)) # Mobius strip (athanasopoulos)
#z = -np.sin(a*t)*(b+np.cos(s))+ np.cos(a*t)*np.sin(s)*np.cos(2*s) # Mobius strip (athanasopoulos)

a=np.sin(t)
b=np.cos(t)
c=np.sin(s)
d=np.cos(s)
x = (-2/15)*(b)*((3*d)-(30*a)+90*(b**4)*a-(60*(b**6)*a)+(5*b*d*a) )
y = (-1/15)*(a)*((3*d)-(3*(b**2)*d)-(48*(b**4)*d)+(48*(b**6)*d)-(60*a)+(5*b*d*a)-(5*(b**3)*d*a)-(80*(b**5)*d*a)+ (80*(b**7)*d*a) )
z = (2/15)*(3+5*b*a)*c

#x = (a - s*np.sin(b*t)*np.sin(b*t))*np.sin(t)  # Klein bottle (wiki)
#y = (a - s*np.cos(b*t)*np.sin(b*t))*np.cos(t)  # Klein bottle (wiki)
#z = (s)*np.cos(b*t)  # Klein bottle (wiki)

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
    ax.set_title('Klein Bottle', fontweight = 'bold', fontsize = 16)
    #ax.set_title('Mobius Strip', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    h = ax.plot_surface(x, y, z, cmap = cm.tab20c, edgecolor = 'k')
    fig.colorbar(h)
    fig.tight_layout()
    a = plt.gca()
    plt.axis('off')
plotter(0, 45)









