
import numpy as np
import matplotlib.pyplot as plt

# Parametrization
f = lambda x, y: np.sin(x)*np.cos(y)
t = np.linspace(-3*np.pi, 3*np.pi, 100)
s = np.linspace(-3*np.pi, 3*np.pi, 100)
x, y = np.meshgrid(t, s)
z = f(x, y)
plt.contour(x, y, z) # points of surface and z=0 plane
# Axes  
fig = plt.figure('Plot and Contour plot')
ax = fig.add_subplot(111, projection='3d')
h = ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = 'c')
fig.colorbar(h)
ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
ax.set_title('Plane', fontweight = 'bold', fontsize = 16)