
import numpy as np
import matplotlib.pyplot as plt

# Parametrization
theta = np.linspace(0 * np.pi, 2 * np.pi, 50)
r = np.linspace(0 * np.pi, 2 * np.pi, 50)
theta, r = np.meshgrid(theta, r)
x = r * np.cos(theta)
y = r * np.sin(theta)
z = r
#Axes set
fig = plt.figure('Parametric Surfaces')
ax = fig.add_subplot(111, projection='3d')
h = ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = None)
fig.colorbar(h)
ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
ax.set_title('Cone', fontweight = 'bold', fontsize = 16)