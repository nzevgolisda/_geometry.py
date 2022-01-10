
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d as Axes3d
from numpy.core.function_base import linspace

# Parametrization
t = np.linspace(0, 2 * np.pi, 40) # Klein bottle (Nordstrand)
s = np.linspace(0, 2 * np.pi, 40) # Klein bottle (Nordstrand)
#t = np.linspace(0, 2 * np.pi, 100) # Mobius strip
#s =  np.linspace(-0.4, 0.4, 80) # Mobius strip
#t = np.linspace(-1 * np.pi, 1 * np.pi, 100) # Variant1
#s = np.linspace(0 * np.pi, 2 * np.pi, 100) # Variant1
#t = np.linspace(0 * np.pi, 2 * np.pi, 100) # Variant2
#s = np.linspace(-1, 1, 100) # Variant2
#t = np.linspace(-1 * np.pi, 1 * np.pi, 100) # Variant3
#s = np.linspace(0 * np.pi, 2 * np.pi, 100) # Variant3

t, s = np.meshgrid(t, s)

#a, b = [1, 0.5] # a>2  #Variant2
#x = (a + b*s*np.cos(b*t)*np.cos(t)) #Variant2
#y = (a + b*s*np.cos(b*t)*np.sin(t)) #Variant2
#z = b*s*np.sin(b*t) #Variant2
#a, b = [0.5, 2**0.5] # a>2
#x = np.cos(t)*(np.cos(a*t)*(b+np.cos(s))+ np.sin(a*t)*np.sin(s)*np.cos(s)) # Klein bottle (Nordstrand)
#y = np.sin(t)*(np.cos(a*t)*(b+np.cos(s))+ np.sin(a*t)*np.sin(s)*np.cos(s)) # Klein bottle (Nordstrand)
#z = -np.sin(a*t)*(b+np.cos(s))+ np.cos(a*t)*np.sin(s)*np.cos(2*s) # Klein bottle (Nordstrand)
a, b, r = [0.5, 2, 60] # Variant1 #r>2
x = (r + np.cos(a*t)*np.sin(s) - np.sin(a*t)*np.sin(b*s))*np.cos(t) #Variant1
y = (r + np.cos(a*t)*np.sin(s) - np.sin(a*t)*np.sin(b*s))*np.sin(t) #Variant1
z = np.sin(a*t)*np.sin(s) + np.cos(a*t)*np.sin(b*s) #Variant1
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
    #ax.set_title('Mobius strip', fontweight = 'bold', fontsize = 16)
    ax.set_title('Klein Bottle', fontweight = 'bold', fontsize = 16)
    ax.view_init(elev=E, azim=A)
    plt.show()
plotter(0, 45)