with open("input.txt", "r") as f:
    data = list((map(int, f.read().split("\n"))))

with open("output.txt", "w") as f:
    f.write(" ".join(list(map(str, sorted(data, key=lambda x: str(x))))))