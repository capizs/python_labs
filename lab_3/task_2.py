s = list(map(int, input().split()))
m = list(map(int, input().split()))
res = []
for i in s:
    if i in m and i not in res:
        res.append(i)
print(len(res))