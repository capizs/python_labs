import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.animation import FuncAnimation

fig, ax = mpl.subplots(figsize=(8, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

t = np.linspace(0, 2*np.pi, 1000)

def init():
    line.set_data([], [])
    return line,

def update(ratio):
    a = 1
    b = ratio
    x = np.sin(a * t)
    y = np.sin(b * t)
    line.set_data(x, y)
    ax.set_title(f'Соотношение частот: {a:.2f}:{b:.2f}')
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0.1, 1, 100),
                    init_func=init, blit=True, interval=50)
mpl.show()