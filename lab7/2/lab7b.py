import math
a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

print("\nТабулювання функції f(x) = |2x + e^(0.1x)| + ln|x|:")
print("x\t\tf(x)")

x = a
while x <= b:
    if x == 0:  # логарифм від 0 не визначений
        print(f"{x:.2f}\tПомилка! ln(0) не існує")
    else:
        f = abs(2 * x + math.exp(0.1 * x)) + math.log(abs(x))
        print(f"{x:.2f}\t{f:.4f}")
    x += h
    