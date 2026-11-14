import random
def suma(N, i=1):
    if i > N:
        return 0
    return i * random.randint(1, i) + suma(N, i + 1)

N = int(input("Введіть N: "))
result = suma(N)
print("Сума добутків:", result)
