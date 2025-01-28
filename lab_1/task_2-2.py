n, s = int(input()), ["1"]
for i in range(2, n + 1):
 s.append(str(i))
 s.insert(0, str(i))
for i in range(n):
 print("".join(s)) 
 s[i], s[-i-1] = " ", " "