a, b, c = map(int, input().split())
if a >= b and a >= c:
 print(f"max: {a}")
elif b >= a and b >= c:
 print(f"max: {b}")
elif c >= a and c >= b:
 print(f"max: {c}")
if a <= b and a <= c:
 print(f"min: {a}")
elif b <= a and b <= c:
 print(f"min: {b}")
elif c <= a and c <= b:
 print(f"min: {c}")