with open("data.txt", "r") as f:
    data = list(map(int, f.read().replace("\n", ",").split(",")))
    print(f"Сумма всех элементов: {sum(data)}")
    print(f"Максимальный элемент: {max(data)}")
    print(f"Минимальный элемент: {min(data)}")