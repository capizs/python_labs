s = input()
d = {}
for i in s:
    if i not in d and i != " ":
        d[i] = s.count(i)
for i in sorted(d, key=d.get, reverse=True)[:3]:
    print(i, d[i])