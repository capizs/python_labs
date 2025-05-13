import numpy as np
import matplotlib.pyplot as mpl

t = np.linspace(0, 10, 1000)
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

mpl.figure(figsize=(12, 8))

for i, (a, b) in enumerate(ratios, 1):
    mpl.subplot(2, 2, i)
    x = np.sin(a * t)
    y = np.sin(b * t)
    mpl.plot(x, y)
    mpl.title(f'Соотношение {a}:{b}')
    mpl.axis('equal')

mpl.tight_layout()
mpl.show()