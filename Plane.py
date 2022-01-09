
import numpy as np
import matplotlib.pyplot as plt

# Parametrization
t = np.linspace(-2 * np.pi, 2 * np.pi, 20)
s = np.linspace(-2 * np.pi, 2 * np.pi, 20)
t, s = np.meshgrid(t, s)
a, b, c = [1, 1, 1]
x0, y0, z0 = [0, 0, 0]
x = t
y = s
z = z0-a*(t-x0)/c-b*(s-y0)/c
# Axes  
fig = plt.figure('Parametric Surfaces')
ax = fig.add_subplot(111, projection='3d')
h = ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = 'c')
fig.colorbar(h)
ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
ax.set_title('Plane', fontweight = 'bold', fontsize = 16)