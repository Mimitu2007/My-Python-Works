import math
a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

print("\nТабулювання функції f(x) = 0.27*sin(6x) + π/2*cos(2πx + 0.1π):")
print("x\t\tf(x)")

for i in range(0, int((b - a) / h) + 1):
    x = a + i * h
    f = 0.27 * math.sin(6 * x) + (math.pi / 2) * math.cos(2 * math.pi * x + 0.1 * math.pi)
    print(f"{x:.2f}\t{f:.4f}")
    