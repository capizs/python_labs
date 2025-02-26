s = list(map(int, input().split()))
m = tuple((min(s), s.index(max(s))))
s[s.index(min(s))] = max(s)
s[m[1]] = m[0]
print(s)