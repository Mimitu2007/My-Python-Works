import numpy as np
data = [
    [100, 101, 102],
    [103, 104, 105]
]
mas = np.array(data)

print(f"Двовимірний масив 2x3:\n{mas}")
total_sum = mas.sum()
print(f"Сума всіх елементів масиву: {total_sum}")
max_element = mas.max()
print(f"Максимальний елемент масиву: {max_element}")