import random

def recursive_sum_products(N):
    """
    Обчислює суму N добутків i * random(1, i) рекурсивно.
    """
    if N <= 0:
        return 0

    current_product = N * random.randint(1, N)
    print(f"Додається: {N} * random(1, {N}) = {current_product}") 
    return current_product + recursive_sum_products(N - 1)

try:
    N_input = int(input("Введіть натуральне число N для обчислення суми: "))
    if N_input < 0:
        print("N повинно бути невід'ємним числом.")
    else:
        total_sum = recursive_sum_products(N_input)
        print(f"\nСума {N_input} добутків (рекурсивно): {total_sum}")
except ValueError:
    print("Помилка: Введено некоректне число.")