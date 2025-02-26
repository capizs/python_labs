s = input()
count, res = 1, ''
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    elif count != 1:
        res += s[i - 1] + str(count)
        count = 1
    else:
        res += s[i - 1]
    if i == len(s) - 1:
        res += s[i]
print(res)