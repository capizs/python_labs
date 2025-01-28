n, s = int(input()), ["1"]

for i in range(2, n + 1):
 s = [str(i)] + s + [str(i)]
 
for i in range( n):
 print("".join(s)) 
 s[i] = " " * len(s[i])
 s[-i-1] = " " * len(s[-i-1])