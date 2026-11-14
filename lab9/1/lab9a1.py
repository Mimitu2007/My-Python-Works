import array as arr
import random

initial_array = arr.array('i', [random.randint(-4, 4) for _ in range(6)])
print(f"Початковий масив: {initial_array}")

arr1 = arr.array('i', [])
arr2 = arr.array('i', [])

for element in initial_array:
    if element > 0:
        arr1.append(element)
    elif element < 0:
        arr2.append(element)

print(f"Масив додатних елементів (arr1): {arr1}")
print(f"Масив від'ємних елементів (arr2): {arr2}")

count_zeros = initial_array.count(0)
print(f"Кількість елементів, що дорівнюють 0: {count_zeros}")

for _ in range(3):
    if len(initial_array) > 0:
        initial_array.pop() 
    else:
        break

    print(f"Масив після видалення останніх 3-х елементів: {initial_array}")