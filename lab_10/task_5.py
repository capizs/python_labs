import numpy as np
import matplotlib.pyplot as mpl
from matplotlib import cm

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = mpl.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm)
ax1.set_title('MSE в линейном масштабе')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')
fig.colorbar(surf1, ax=ax1, shrink=0.5)

ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, np.log10(Z+1), cmap=cm.coolwarm)
ax2.set_title('MSE в логарифмическом масштабе (Z)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log10(MSE)')
fig.colorbar(surf2, ax=ax2, shrink=0.5)

mpl.tight_layout()
mpl.show()