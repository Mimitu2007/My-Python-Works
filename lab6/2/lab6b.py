import random
a = int(input("Введіть початок діапазону a: "))
b = int(input("Введіть кінець діапазону b: "))

num = random.randint(a, b)
print("Випадкове число:", num)
print("Квадрат числа:", num ** 2)
print("Куб числа:", num ** 3)