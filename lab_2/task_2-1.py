s = input()
res = ''
for i in range(len(s)):
    if s[i].isdigit():
        res += s[i - 1] * (int(s[i]) - 1)
    else:
        res += s[i]
print(res)