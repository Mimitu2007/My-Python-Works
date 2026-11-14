import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
N = 50
x = 10
A = set()
for i in range(1, N + 1):
    if is_prime(i):
        A.add(i)
random_list = [random.randint(1, N) for _ in range(x)]
B = set(random_list)
prime_random = A & B
print(f"Прості числа до {N}: {A}")
print(f"Випадкові числа: {B}")
print(f"Спільні прості числа (Перетин A і B): {prime_random}")