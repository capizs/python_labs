with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().split("\n")
    data = sorted(data, key=lambda x: x.split()[2])

with open("max_age.txt", "w", encoding="utf-8") as f:
    f.write(data[-1])\

with open("min_age.txt", "w", encoding="utf-8") as f:
    f.write(data[0])