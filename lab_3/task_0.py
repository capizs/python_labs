s = list(map(int, input().split()))
res = []
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        res.append(s[i + 1])
print(res)