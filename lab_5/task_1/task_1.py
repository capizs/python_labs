with open("input.txt", "r") as f:
    data = list(map(int, f.read().split()))

res = 1
for i in data:
    res *= i

with open("output.txt", "w") as f:
    f.write(str(res))