import numpy as np

a = np.arange(16).reshape(4,4)
a[[0, 2]] = a[[2, 0]]
print(a)