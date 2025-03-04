s = input()
d = {}
for i in s:
    if int(i) not in d:
        d[int(i)] = 1
    else:
        d[int(i)] = d[int(i)] + 1
m = sorted(d, key=d.get, reverse=True)
print({m[0]: d[m[0]], m[1]: d[m[1]], m[2]: d[m[2]]})