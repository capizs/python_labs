import numpy as np

x = np.array(list(map(int, input().split())))
res = []
for i in range(1, len(x)):
    if x[i-1] == 0:
        res.append(x[i])
print(max(res))