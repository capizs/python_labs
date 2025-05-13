import numpy as np

s = np.random.normal(size=(10, 4))
k = np.array(s[0:5, : ])
print(f"Минимальное значение: {np.min(s)}")
print(f"Максимальное значение: {np.max(s)}")
print(f"Среднее значение: {np.mean(s)}")
print(f"Стандартное отклонение: {np.std(s)}")
print("Первые 5 строк:")
print(k)

