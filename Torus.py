
import numpy as np
import matplotlib.pyplot as plt

# Parametrization
theta = np.linspace(0 * np.pi, 2 * np.pi, 50)
phi = np.linspace(0 * np.pi, 2 * np.pi, 50)
theta, phi = np.meshgrid(theta, phi)
x0, y0, z0, r, r1 = [0, 0, 0, 1, 5]
x = x0 + (r1 + r * np.cos(theta))*np.cos(phi)
y = y0 + (r1 + r * np.cos(theta))*np.sin(phi)
z = z0 + (r1 + r * np.sin(theta))
#Axes set
fig = plt.figure('Parametric Surfaces')
ax = fig.add_subplot(111, projection='3d')
h = ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = None)
fig.colorbar(h)
ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
ax.set_title('Torus', fontweight = 'bold', fontsize = 16)