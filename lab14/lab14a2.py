import math

radius_circumscribed = lambda a, b: math.sqrt(a**2 + b**2) / 2

radius_inscribed = lambda a, b: a / 2 if a == b else "Неможливо (прямокутник не є квадратом)"

try:
    side_a = float(input("Введіть довжину сторони A: "))
    side_b = float(input("Введіть довжину сторони B: "))

    if side_a <= 0 or side_b <= 0:
        print("Довжини сторін мають бути додатніми.")
    else:
        R = radius_circumscribed(side_a, side_b)
        r = radius_inscribed(side_a, side_b)

        print(f"\nРадіус описаного кола (R): {R}")
        print(f"Радіус вписаного кола (r): {r}")
except ValueError:
    print("Помилка: Введено некоректні дані.")