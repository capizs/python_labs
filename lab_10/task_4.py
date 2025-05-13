import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.widgets import Slider

fig = mpl.figure(figsize=(12, 8))
ax = mpl.axes([0.1, 0.4, 0.8, 0.5])
mpl.subplots_adjust(bottom=0.3)

freq1, amp1 = 1.0, 1.0
freq2, amp2 = 2.0, 0.5

x = np.linspace(0, 4*np.pi, 1000)
line1, = ax.plot(x, amp1*np.sin(freq1*x), 'r-', label='Волна 1')
line2, = ax.plot(x, amp2*np.sin(freq2*x), 'b-', label='Волна 2')
line_sum, = ax.plot(x, amp1*np.sin(freq1*x) + amp2*np.sin(freq2*x), 'g-', label='Сумма')
mpl.legend()

ax_freq1 = mpl.axes([0.1, 0.2, 0.35, 0.03])
ax_amp1 = mpl.axes([0.1, 0.15, 0.35, 0.03])
ax_freq2 = mpl.axes([0.1, 0.1, 0.35, 0.03])
ax_amp2 = mpl.axes([0.1, 0.05, 0.35, 0.03])

s_freq1 = Slider(ax_freq1, 'Частота 1', 0.1, 5.0, valinit=freq1)
s_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=amp1)
s_freq2 = Slider(ax_freq2, 'Частота 2', 0.1, 5.0, valinit=freq2)
s_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=amp2)

def update(val):
    f1 = s_freq1.val
    a1 = s_amp1.val
    f2 = s_freq2.val
    a2 = s_amp2.val
    line1.set_ydata(a1*np.sin(f1*x))
    line2.set_ydata(a2*np.sin(f2*x))
    line_sum.set_ydata(a1*np.sin(f1*x) + a2*np.sin(f2*x))
    fig.canvas.draw_idle()

s_freq1.on_changed(update)
s_amp1.on_changed(update)
s_freq2.on_changed(update)
s_amp2.on_changed(update)

mpl.show()