n, c = int(input()), 0
s = [i for i in range(1, n + 1)]
for i in range(n):
 print(*s[:n-c])
 c += 1