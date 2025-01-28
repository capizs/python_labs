n = int(input())
s = [[1], [1, 1]]
end = n * 2 + 1
for i in range(n - 1):
 r = []
 for j in range(len(s[-1])-1):
  r.append(s[-1][j] + s[-1][j+1])
 r = [1] + r + [1]
 s.append(r)
for i in s:
 print(" " * ((end - (len(i) * 2 - 1)) // 2) , *i)