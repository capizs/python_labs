import numpy as np
import matplotlib.pyplot as mpl
from scipy.special import legendre

mpl.figure(figsize=(10, 7))
x = np.linspace(-1, 1, 500)

for n in range(1, 8):
    y = legendre(n)(x)
    mpl.plot(x, y, label=f'n = {n}')

mpl.title('Полиномы Лежандра')
mpl.xlabel('x')
mpl.ylabel('P_n(x)')
mpl.grid(True)
mpl.legend()
mpl.show()