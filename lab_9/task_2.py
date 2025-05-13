import numpy as np

x = np.array(list(map(int, input().split())))
num = np.array([], "int32")
count = np.array([], "int32")
c = 1

for i in range(1, len(x)):
    if x[i-1]==x[i]:
        c += 1
        if i == len(x) - 1:
            num = np.append(num, x[i])
            count = np.append(count, c)
            c = 1
    else:
        num = np.append(num, x[i-1])
        count = np.append(count, c)
        c = 1
        if i == len(x) - 1:
            num = np.append(num, x[i])
            count = np.append(count, c)
            c = 1

print((num, count))