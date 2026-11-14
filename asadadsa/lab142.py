import math

D_to_R = lambda D: D / 2

volume_cylinder = lambda D, H: math.pi * (D_to_R(D)**2) * H

surface_area_cylinder = lambda D, H: 2 * math.pi * D_to_R(D) * H + 2 * math.pi * (D_to_R(D)**2)

try:
    diameter = float(input("Введіть діаметр основи циліндра (D): "))
    height = float(input("Введіть висоту циліндра (H): "))

    if diameter <= 0 or height <= 0:
        print("Діаметр і висота мають бути додатніми.")
    else:
        V = volume_cylinder(diameter, height)
        S = surface_area_cylinder(diameter, height)

        print(f"\nДіаметр (D): {diameter}, Висота (H): {height}")
        print(f"Об'єм циліндра (V): {V:.2f}")
        print(f"Площа повної поверхні (S): {S:.2f}")
except ValueError:
    print("Помилка: Введено некоректне число.")