import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

from matplotlib import cm
from matplotlib.ticker import LinearLocator



N = 1024
n = np.arange(N)

theta0 = 0.1*pi
a0 = 0.5

z0 = np.real(a0*np.exp(1j*theta0))
print(z0)

arange = np.linspace(0,1,N)
thetarange = np.linspace(0,pi,N)

Z = np.real(np.outer(arange,np.exp(1j*thetarange)))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

Loss_matrix = (Z-z0)**2

# Make data.

X, Y = np.meshgrid(arange, thetarange)
Z = Loss_matrix

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()