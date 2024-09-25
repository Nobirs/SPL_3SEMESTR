import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for x and y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define the functions
Z1 = np.sign(X) * (np.abs(X)) ** (1 / 4) + np.sign(Y) * (np.abs(Y)) ** (1 / 4)
Z2 = X**2 - Y**2
Z3 = 2*X + 3*Y
Z4 = 2 + 2*X + 2*Y - X**2 - Y**2

# Create a 3D plot
fig = plt.figure(figsize=(15, 12))

# First function: z = x^0.25 + y^0.25
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis', edgecolor='none')
ax1.set_title('z = x^0.25 + y^0.25')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')

# Second function: z = x^2 - y^2
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma', edgecolor='none')
ax2.set_title('z = x^2 - y^2')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.set_zlabel('Z axis')

# Third function: z = 2x + 3y
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='inferno', edgecolor='none')
ax3.set_title('z = 2x + 3y')
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')
ax3.set_zlabel('Z axis')

# Fourth function: z = 2 + 2x + 2y - x^2 - y^2
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='magma', edgecolor='none')
ax4.set_title('z = 2 + 2x + 2y - x^2 - y^2')
ax4.set_xlabel('X axis')
ax4.set_ylabel('Y axis')
ax4.set_zlabel('Z axis')

# Show the plot
plt.tight_layout()
plt.show()
